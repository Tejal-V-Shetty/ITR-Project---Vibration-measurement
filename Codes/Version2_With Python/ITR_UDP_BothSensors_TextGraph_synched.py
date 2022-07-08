import socket
import datetime as dt
import keyboard
import random
import sys
import pandas as pd
import select

UDP_IP1 = "192.168.43.50"
UDP_IP2 = "192.168.43.250"
UDP_IP_R = "0.0.0.0"
UDP_PORT1 = 8888
UDP_PORT2 = 4210
file_name='C:\\Users\\Tejal\\Documents\\ITR_Readings\\Readings_'+dt.datetime.now().strftime('%d-%m--%Hh%Mm')+'.csv'
graphline1="..........---------------------------------------------------------------------------------------------------"

#Graphline- 1 to 100 | 100 onwards in steps of 100 -> Limit = 7000
graphline="■■■■■■■■■■███████████████████████████████████████████████████████████"

#Arrays to contain timestamp and sensor values, along with iteration count
xs = []
ys = []
ys2 = []
count=0

MESSAGE1 = b"S1"
MESSAGE2 = b"S2"

def writetofile():
    data= pd.DataFrame({'Timestamp':xs,'Sensor 1':ys,'Sensor 2':ys2})
    data.to_csv(file_name)

#Sensor 1 socket setup
try:
    sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
    sock.bind((UDP_IP_R, UDP_PORT1))
    print("UDP target IP: %s" % UDP_IP1)
    print("UDP target port: %s" % UDP_PORT1)
    print("Message: %s" % MESSAGE1)
    sock.sendto(MESSAGE1, (UDP_IP1, UDP_PORT1))
    sock.setblocking(0)
except:
    print("Couldn't connect to sensor 1")

#Sensor 2 socket setup
try:
    sock2 = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
    sock2.bind((UDP_IP_R, UDP_PORT2))
    print("UDP target IP: %s" % UDP_IP2)
    print("UDP target port: %s" % UDP_PORT2)
    print("Message: %s" % MESSAGE2)
    sock2.sendto(MESSAGE2, (UDP_IP2, UDP_PORT2))
    sock2.setblocking(0)
except:
    print("Couldn't connect to sensor 2")

while True:
    # Ready waits for an incoming signal from the sensor socket specified. Timeout =0.1sec
    ready = select.select([sock], [], [], 0.1)
    ready2 = select.select([sock2], [], [], 0.1)
    if ready[0] or ready2[0]:
        time=dt.datetime.now().strftime('%H:%M:%S.%f')  #Timestamp for signal reception
        time=time[:-3]  #Round off the microseconds to 3 digits
        if ready[0]:
            data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        else:
            data = b'0'     #In the case of only the second sensor geting a signal
        if ready2[0]:
            data2, addr2 = sock2.recvfrom(1024) # buffer size is 1024 bytes
        else:
            data2 = b'0'    #In the case of only the first sensor geting a signal
        #Sensor 1 graph mapping
        sval=data.decode('UTF-8')   #Convert from binary hexcode to string
        sensorval=int(sval)     #Convert from string to int
        graphval=0
        if(sensorval<100):      #If the value is less than 100, it's represented as a multiple of 10
            graphval=sensorval/10
        else:                   #If the value is greater than 100, it's represented as a multiple of 100
            graphval=10+(sensorval-100)/100
            if(graphval>60):
                graphval=60
                
        #Sensor 2 graph mapping
        sval2=data2.decode('UTF-8')
        sensorval2=int(sval2)
        graphval2=0
        if(sensorval2<100):
            graphval2=sensorval2/10
        else:
            graphval2=10+(sensorval2-100)/100
            if(graphval2>60):
                graphval2=60
        
        print(time,"S1= %5d %-60s" % (sensorval,graphline[0:int(graphval)]),"S2= %5d " % sensorval2,graphline[0:int(graphval2)])
        #Recording the  timestamp and sensor values in the respective arrays
        xs.append(time)
        ys.append(sensorval)
        ys2.append(sensorval2)
        count+=1

    #Write to an external csv file every 20 iterations
    if count>=20:
            writetofile()
            count=0

    if keyboard.is_pressed('r'):        #Press 'r' to reconnect to sensor 1
        sock.sendto(MESSAGE1, (UDP_IP1, UDP_PORT1))
        print("Reconnecting: %s" % MESSAGE1)   
    elif keyboard.is_pressed('t'):      #Press 't' to reconnect to sensor 2
        sock2.sendto(MESSAGE2, (UDP_IP2, UDP_PORT2))
        print("Reconnecting: %s" % MESSAGE2)
    elif keyboard.is_pressed('q'):      #Press 'q' to exit
        sys.exit()
