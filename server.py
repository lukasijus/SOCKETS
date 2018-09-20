#!/usr/bin/env python

import socket
from datetime import datetime
import select
import keyboard

K3 = bytes('K3|    |\n', 'utf-8')
A1 = bytes('A1|123456789ABCDF|         |\n', 'utf-8')
A1_2 = bytes('A1|2312359A4534CDG|         |\n', 'utf-8')
A1_3 = bytes('A1|749376789GDLSL|         |\n', 'utf-8')

TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024  

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()

conn.setblocking(0)
print ('Connection address:', addr)
print(conn.setblocking(0))
tm = -1
while True:
    t = datetime.now()
    print(t.second)
    if t.minute > tm + 1:
        conn.send(K3)
        tm = t.minute
    if keyboard.is_pressed('s'):
        print('Sending Roll ID!')
        conn.send(A1)
    if keyboard.is_pressed('a'):
        print('Sending Roll ID!')
        conn.send(A1_2)
    if keyboard.is_pressed('d'):
        print('Sending Roll ID!')
        conn.send(A1_3)
    ready = select.select([conn], [], [], 1)
    if ready[0]:
        data = conn.recv(254)
        if not data: break
        print ("received data:", data)
 # echo
conn.close()
