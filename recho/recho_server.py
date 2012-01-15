"""
echo server, usage:

 python echo_server.py <port>

Port is optional, default: 50000
"""

import socket 
import sys
import os
import subprocess

host = '' 
port = 50000 

if len(sys.argv) > 1:
    port = int(sys.argv[1]) 

backlog = 5 
size = 1024 


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 


s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((host,port)) 

print 'echo_server listening on port', port
s.listen(backlog) 

while True: 
    client, address = s.accept() 
    data = client.recv(size) 
    if data: 
        p=subprocess.Popen("whoami", stdout=subprocess.PIPE)
        me=p.stdout.read()
        me=me.rstrip(os.linesep)
        client.send('%s: %s' %(me, data))
    print 'from %s: %s' % (address, data)
    client.close()
