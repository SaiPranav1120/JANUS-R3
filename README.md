## Task 1 - GCS

This program receives telemetry data from an XBee3, extracts the latitude, longitude, and altitude, and displays the flight path on a live 3D graph.

### Functioning

The program is designed to receive telemetry packets from an XBee device. The incoming data is received as bytes and decoded into a text string. The string is then split using commas so that each telemetry value can be accessed individually.

### Telemetry Formatting :

Timestamp, State, Temperature, Pressure, Altitude,
Battery Voltage, Battery Current, Latitude, Longitude,
Prev_CMD_echo

Index 4 → Altitude
Index 7 → Latitude
Index 8 → Longitude

## XBee Implementation

The Digi XBee Python library is used to communicate with the XBee device. XBeeDevice is used to create the connection, and a data-received callback is registered so that the program can process telemetry whenever a new packet arrives.

[ device.add_data_received_callback(receive_data_callback) ]

The callback is automatically called when the XBee receives a new packet.

### Plotting

Matplotlib is used to create the 3D graph. Longitude is used as the X-axis, latitude as the Y-axis, and altitude as the Z-axis. Every new telemetry packet adds another point to the stored flight path, allowing the trajectory to be visualized as the data arrives.

### Simulation

The code has two functions. The first is the default real_xbee function which works if you connect an xbee device to the computer.
If you don't have one but wanna check the other funxns, I just added a simulation kinda thing for a good measure. you can replace the real_xbee with simulate().


## Task 2

I don't think I got enough time to complete it. I wasted a lotta time trying to fine tune the pcb but finally left it unfinished. (wasted 2 hrs ;( )


## Task 3

I tried to design the pcb but I found out that I need to have some practice with routing. I used to do this like 5 years ago in EasyEDA but then forgot most of it. I left it unfinished. Sorry :(.
