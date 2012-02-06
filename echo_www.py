"""
hello_www.py - minimal web server + web application
"""

import socket 
import sys
import time
import datetime
import os
import getpass
import string

current_time = time.time()
current_time_readable = datetime.datetime.now()


page = """
HTTP/1.0 200 OK
Content-Type text/html

<html>
<head><p>Current time: <b>%s</b> on host <b>%s</b> </p></head>
<body>
Hello, world!  Hello, user %s 
requesting URL http:/%s
</body>
</html>
"""

host = '' 
port = 8082 # 8081 # different default port than thirty_minute_webserver

# optional command line argument: port 
if len(sys.argv) > 1:
    port = int(sys.argv[1])

backlog = 5 
size = 1024 

# server's listener socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

current_host=socket.gethostname()
current_user=getpass.getuser()


# Release listener socket immediately when program exits, 
# avoid socket.error: [Errno 48] Address already in use
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((host,port)) 

print 'echo_www listening on port', port
s.listen(backlog) 

while True: # just keep serving page to any client that connects
    client, address = s.accept() # create client socket
    # client.recv(size) # HTTP request - not too big!  Just ignore contents
    # client.send(page) # HTTP response - same for any request
    info=client.recv(size)
    info_url_split = info.split()
    client.send(page %(current_time_readable, current_host, current_user, info_url_split[1]))
    client.close()
