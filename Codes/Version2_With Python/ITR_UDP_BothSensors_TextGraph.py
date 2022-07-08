import socket
import datetime as dt
import keyboard
import random
import sys
import pandas as pd
import select

#Readings- 1-Initial, 2-Lesser delay,3, 4-Modified code+delay200ms
UDP_IP1 = "192.168.43.50"#250   ,253
UDP_IP2 = "192.168.43.250"
UDP_IP_R = "0.0.0.0"
UDP_PORT1 = 8888#4210
UDP_PORT2 = 4210
file_name='C:\\Users\\Tejal\\Documents\\Programs\\Readings_'+dt.datetime.now().strftime('%d-%m--%Hh%Mm')+'.csv'
graphline1="..........---------------------------------------------------------------------------------------------------"
#Graphline- 1 to 100 | 100 onwards in steps of 100
graphline="■■■■■■■■■■███████████████████████████████████████████████████████████████████████████████████████████████████"
flag=0

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
    flag=1
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
    flag=2

while True:
    ready = select.select([sock], [], [], 0.1)
    ready2 = select.select([sock2], [], [], 0.1)
    if ready[0]:
        time=dt.datetime.now().strftime('%H:%M:%S.%f')
        time=time[:-3]
        data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
        sval=data.decode('UTF-8')
        sensorval=int(sval)
        graphval=0
        if(sensorval<100):
            graphval=sensorval/10
        else:
            graphval=10+(sensorval-100)/100
            if(graphval>100):
                graphval=100
        print(time,"S1= %5d " % sensorval,graphline[0:int(graphval)])
        xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
        ys.append(sensorval)
        ys2.append(0)
        count+=1        
    if ready2[0]:
        time2=dt.datetime.now().strftime('%H:%M:%S.%f')
        time2=time2[:-3]
        data2, addr2 = sock2.recvfrom(1024) # buffer size is 1024 bytes
        sval2=data2.decode('UTF-8')
        sensorval2=int(sval2)
        graphval2=0
        if(sensorval2<100):
            graphval2=sensorval2/10
        else:
            graphval2=10+(sensorval2-100)/100
            if(graphval2>100):
                graphval2=100
        print(time2,"S2= %5d " % sensorval2,graphline[0:int(graphval2)])
        xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
        ys.append(0)
        ys2.append(sensorval2)
        count+=1
    if count>=20:
            writetofile()
            count=0
    if keyboard.is_pressed('r'):            
        sock.sendto(MESSAGE1, (UDP_IP1, UDP_PORT1))
        print("Message: %s" % MESSAGE1)
    elif keyboard.is_pressed('t'):            
        sock.sendto(MESSAGE2, (UDP_IP2, UDP_PORT2))
        print("Message: %s" % MESSAGE2)
    elif keyboard.is_pressed('q'):
        sys.exit()
