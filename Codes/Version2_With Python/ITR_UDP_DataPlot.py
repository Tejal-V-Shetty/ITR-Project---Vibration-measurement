import socket
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.animation as animation
import keyboard
import random

UDP_IP1 = "192.168.43.50"
UDP_IP2 = "192.168.43.35"
UDP_IP_R = "0.0.0.0"
UDP_PORT1 = 8888
UDP_PORT2 = 8887

# Create figure for plotting
fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)
xs = []
ys = []
ys2 = []

    
MESSAGE = b"Sensor 1"

def animate(i, xs, ys):
    if keyboard.is_pressed('q'):
        sys.exit()
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    sval=data.decode('UTF-8')
    sensorval=int(sval)
    print(sensorval)
    
    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(sensorval)

    # Limit x and y lists to 50 items
    xs = xs[-20:]
    ys = ys[-20:]
    
    # Draw x and y lists
    ax1.clear()
    ax2.clear()
    ax.plot(xs, ys)
    ax2.plot(xs, ys)

    # Format plot
    ax1.tick_params(axis='x', labelrotation=90)
    ax2.tick_params(axis='x', labelrotation=90)
    plt.subplots_adjust(bottom=0.30)
    ax1.set_title('Vibration data-Sensor 1')
    ax2.set_title('Vibration data-Sensor 2')
    ax1.set_ylabel('Intensity')
    ax2.set_ylabel('Intensity')

print("UDP target IP: %s" % UDP_IP1)
print("UDP target port: %s" % UDP_PORT1)
print("message: %s" % MESSAGE)
sock = socket.socket(socket.AF_INET, # Internet
                    socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP_R, UDP_PORT1))
sock.sendto(MESSAGE, (UDP_IP1, UDP_PORT1))
while True:
    # Set up plot to call animate() function periodically
    ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=100)
    plt.show()
    if keyboard.is_pressed('q'):
        sys.exit()
