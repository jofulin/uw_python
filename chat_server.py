"""
Based on Daniel Zappala's http://ilab.cs.byu.edu/python/code/echoserver-select.py
Add print statements to show what's going on.
Use SO_REUSEADDR to avoid 'Address already in use' errors
Add timeout
make style similar to our recho_clien

An echo server that uses select to handle multiple clients at a time.
Entering any line of input at the terminal will exit the server.
"""

import select
import socket
import sys
import time
import datetime

host = ''
port = 50003 # different port than other samples, all can run on same server

if len(sys.argv) > 1:
    port = int(sys.argv[1])

backlog = 5
size = 1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create a listener socket

# Release listener socket immediately when program exits, 
# avoid socket.error: [Errno 48] Address already in use
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((host,port))

print 'echo_server listening on port %s, to exit type return ' % port
server.listen(backlog)

timeout = 10 # seconds
input = [server,sys.stdin] # a list
ips=[]
running = True
while running:
    inputready,outputready,exceptready = select.select(input,[],[],timeout)

    # timeout
    if not inputready:  
        print 'Server running at %s' % datetime.datetime.now()

    for s in inputready:

        if s == server:
            # handle the server socket
            client, address = server.accept()
            input.append(client)
            ips.append(client)
            print 'accepted connection from', address

        elif s == sys.stdin:
            # handle standard input
            junk = sys.stdin.readline()
            running = False
            print 'Input %s from stdin, exiting.' % junk.strip('\n')

        elif s: # client socket
            data = s.recv(size)
            print '%s: %s' % (s.getpeername(), data.strip('\n'))
            if data:
                s.send('%s: %s' %(s.getpeername(), data.strip('\n')) )

                print 'BROCASTING TO ALL CLIENTS: %s' %data
                for s2 in ips:
                    s2.send('MESSAGE SENT FROM %s at %s: %s'  %(s.getpeername(), datetime.datetime.now(), data))
            else:
                s.close()
                print 'closed connection'
                input.remove(s)
                ips.remove(s2)

s.close()
