# Program details

## Piezoelectric only
- Currently not being used
- Contains code to receive analog input from the piezoelectric ceramic disks through voltage measurement chip
- Contains 2 versions:
	1. Sends data to Ubidots over WiFi connection
	2. Displays sensor value on serial monitor (No WiFi)

## Vibration Sensor + Piezo
- Currently not being used
- Contains code to read analog input from ceramic disks, and digital(PulseIn) reading from a vibration sensor chip
- Contains 2 versions:
	1. Sends data to Ubidots over WiFi connection
	2. Displays sensor value on serial monitor (No WiFi)

## Version 2 - With Python
- Contains code to read digital(PulseIn) data from a vibration sensor chip and transmit it to a Python socket recipient
- Protocol used : UDP
- Contains 4 codes :
	1. UDP_Send : Reads and sends data from sensor module 1 (Local port: 8888)
	2. UDP_Send 2 : Reads and sends data from sensor module 2 (Local port: 4210)
	3. UDP_Data_Plot : Receives data from both sensors and plots it on a graph 
		- Has latency issues due to animation function
		- Has synching issues, with both sensors needing to send data and not just 1
	4. UDP_SingleSensor_TextGraph : Receives data from a single sensor and plots it on a text based graph