
# coding: utf-8

# In[63]:

import socket
import sys
import time


def writer(timer,off_timer,fulldata, x_vector):
    off_timer = int(off_timer)
    #print timer, off_timer
    if timer == 0:
        x_vector.extend('[')
    if timer < off_timer:
        x_vector.extend(fulldata)
        timer = timer + 1
        #print 'timer = '+str(timer)
    if timer == (off_timer-2):
        x_vector.extend(']')
        print x_vector
        x_f = open('X.txt','a')
        str = str(x_vector)
        print str
        x_f.write(str)
        x_f.close()
    return timer,x_vector

HOST = '142.0.198.4'   # Symbolic name meaning all available interfaces
PORT = 4551 # Arbitrary non-privileged port


check_device = 0
split_data = []
off_timer = 0
x_vector=[]
# Datagram (udp) socket
try :
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print 'Socket created'
except socket.error, msg :
    print 'Failed to create socket. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()


# Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error , msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()

print 'Socket bind complete'
#plt.show(())
#now keep talking with the client
while 1:
    # receive data from client (data, addr)
    package = s.recvfrom(1024)
    data = package[0]
    addr = package[1]

    if not data:
        break

    fulldata=[]

    reply = 'OK...' + data
    package_data = data.split(',')
    print package_data
    if package_data[0]=='0':
        device_id = package_data[1]
        if device_id == '1' and check_device == 0:
            split_data.extend(package_data[2:8])
            check_device = 1
        elif device_id == '2' and check_device == 1:
            split_data.extend(package_data[2:8])
            fulldata = split_data
            split_data = []
            check_device = 0
            timer,x_vector = writer(timer,off_timer,fulldata,x_vector)
            #print fulldata
        else:
            #print 'Deivce synchronization error'
            pass
        #print 'Message[' + addr[0] + ':' + str(addr[1]) + '] - ' + data.strip()
    elif package_data[0]=='1':
        timer = 0
        off_timer = package_data[2]
        f = open('y.txt','a')
        f.write('[%s]'%package_data[1])
    else:
        pass



        s.close()


# In[ ]:



x_f = open('X.txt','a')
str = 12
print str
x_f.write(str)
x_f.close()


# In[ ]:

