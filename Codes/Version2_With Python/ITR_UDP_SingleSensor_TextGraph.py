import socket
import datetime as dt
import keyboard
import random
import sys
import pandas as pd
import select

#Readings- 1-Initial, 2-Lesser delay,3, 4-Modified code+delay200ms
UDP_IP1 = "192.168.43.50"#250   ,253
UDP_IP_R = "0.0.0.0"
UDP_PORT1 = 8888#4210
file_name='C:\\Users\\Tejal\\Documents\\Programs\\Readings_'+dt.datetime.now().strftime('%d-%m--%Hh%Mm')+'.csv'
graphline1="..........---------------------------------------------------------------------------------------------------"
#Graphline- 1 to 100 | 100 onwards in steps of 100
graphline="■■■■■■■■■■███████████████████████████████████████████████████████████████████████████████████████████████████"
flag=0

xs = []
ys = []
count=0

MESSAGE = b"S1"

def writetofile():
    data= pd.DataFrame({'Timestamp':xs,'Sensor 1':ys})
    data.to_csv(file_name)

#Sensor 1 socket setup
try:
    sock = socket.socket(socket.AF_INET, # Internet
                        socket.SOCK_DGRAM) # UDP
    sock.bind((UDP_IP_R, UDP_PORT1))
    print("UDP target IP: %s" % UDP_IP1)
    print("UDP target port: %s" % UDP_PORT1)
    print("Message: %s" % MESSAGE)
    sock.sendto(MESSAGE, (UDP_IP1, UDP_PORT1))
    sock.setblocking(0)
except:
    print("Couldn't connect to sensor 1")
    flag=1

while True:
    ready = select.select([sock], [], [], 1)
    if ready[0]:
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
        print(dt.datetime.now().strftime('%H:%M:%S.%f'),"S1= %5d " % sensorval,graphline[0:int(graphval)])
        xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
        ys.append(sensorval)
        count+=1
        if count>=20:
            writetofile()
            count=0
    if keyboard.is_pressed('r'):            
        sock.sendto(MESSAGE, (UDP_IP1, UDP_PORT1))
        print("Message: %s" % MESSAGE)
    if keyboard.is_pressed('q'):
        sys.exit()
    
