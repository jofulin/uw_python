
import select
import socket
import sys
import time
import datetime


host = 'localhost'
port = 50003
size = 1024

nargs = len(sys.argv)
if nargs > 1:
    host = sys.argv[1]
if nargs > 2:
    port = int(sys.argv[2])

text = ''
timeout = 10 # seconds

#open socket for sending to the server
s = socket.socket(socket.AF_INET,
                      socket.SOCK_STREAM)
s.connect((host,port))

input = [s, sys.stdin]

# print ">  "
while True :
    inputready,outputready,exceptready = select.select(input,[],[],timeout)
    for msg in inputready:
        if msg == s:
            text = s.recv(size)
            print text
        elif msg == sys.stdin:
            read_in = raw_input("> ")
            if read_in :
                s.send(read_in)
            else :
                s.close()

