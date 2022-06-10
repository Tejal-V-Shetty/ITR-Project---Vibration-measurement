# ITR-Project---Vibration-measurement
A repository containing the details and resources for the vibration measurement project.

## Aim
To detect and record vibration in multiple parts of a vehicle simultaneously using vibration sensors.

## Overview 
The sensors receive power from the Arduino, which in itself is powered by a small portable battery.<br>
The pins receive the signal from the sensors.<br>
The signal is then transmitted to an external system, or uploaded to a server, so as to access it using other devices (the choice of upload will be finalized after looking at which one is practically feasible).<br>
Fourier transforms and other signal conditioning is performed, following which, the data is represented using Python's graphing libraries, and also recorded using the NumPy and Pandas libraries. 

## Components
- Arduino
- Bread board
- Voltage measurement boards X4
- Piezoelectric disks X4
- Jumper cables
- Power bank
- SW-420 vibration sensor
- SW-18015P vibration sensor
- Neodymium magnets

## Tools
- Soldering iron

## Programs
### WiFi enabled NodeMCU code
- States the protocol used
- Has 2 variants : 
  - Only piezoelectric sensor
  - Both piezoelectric and vibration sensors

### Serial Monitor output without WiFi
- Contains code used only for reading the sensor data and displaying it in the serial monitor 
- Used only for testing pursposes

<br>
<img src="https://github.com/Tejal-V-Shetty/ITR-Project---Vibration-measurement/blob/main/Assets/ITR_Project_Details.jpg" alt="Lumen Alert" width=405>
