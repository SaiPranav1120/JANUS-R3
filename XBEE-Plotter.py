from digi.xbee.devices import XBeeDevice
import matplotlib.pyplot as plt
import time

PORT = "/dev/ttyUSB0"
BAUD_RATE = 9600
#port can be /dev/ttyUSB* in Ubuntu systems
#lists to store the telem data
latitudes = []
longitudes = []
altitudes = []

#graphing
plt.ion()

fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")

ax.set_xlabel("Longitude")
ax.set_ylabel("Latitude")
ax.set_zlabel("Altitude (m)")
ax.set_title("Live Telemetry")


#the main part n *prolly* fun
def process_telemetry(data):

    # Spliting the comma-separated packets
    values = data.split(",")

    # Extract required fields
    altitude = float(values[4])
    latitude = float(values[7])
    longitude = float(values[8])

    # Store them
    latitudes.append(latitude)
    longitudes.append(longitude)
    altitudes.append(altitude)

    # Redraw graph
    ax.clear()

    ax.plot(
        longitudes,
        latitudes,
        altitudes,
        marker="o"
    )

    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")
    ax.set_zlabel("Altitude (m)")
    ax.set_title("Live Telemetry")

    plt.draw()
    plt.pause(0.01)


def receive_data_callback(xbee_message):

    raw_data = xbee_message.data

    data = raw_data.decode("utf-8")
# decoding raw data into text
    print("Received:", data)

    process_telemetry(data)

#simulatiom w/o an ackshual xbee
def simulate():

    print("Running simulation...")

    for i in range(100):

        timestamp = int(time.time())
        state = 1
        temperature = 25.0
        pressure = 101325.0

        #decreasing altitude
        altitude = 700 - i * 5

        battery_voltage = 12.0
        battery_current = 0.5
        #changing position
        latitude = 17.3850 + i * 0.0001
        longitude = 78.4867 + i * 0.0001

        command = "NONE"

        data = (
            f"{timestamp},{state},{temperature},"
            f"{pressure},{altitude},"
            f"{battery_voltage},{battery_current},"
            f"{latitude},{longitude},{command}"
        )

        print("Received:", data)

        process_telemetry(data)

        time.sleep(0.1)

    plt.ioff()
    plt.show()


#dis if i get a riyall xbee
def real_xbee():

    device = XBeeDevice(PORT, BAUD_RATE)

    try:

        device.open()

        print("XBee connected!")
        print("Waiting for telemetry...")

        # Tell Digi XBee library to call our function
        # whenever data arrives
        device.add_data_received_callback(
            receive_data_callback
        )

        while True:
            time.sleep(1)

    except KeyboardInterrupt:

        print("Stopping...")

    finally:

        if device.is_open():
            device.close()


#simuacion

real_xbee()

# For NO-actual XBee hardware, replace: real_xbee()    with: simulate()
