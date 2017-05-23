'''
Introduction to Networking(TCP)
TCP Connections / Sockets
an internet/network socket is an endpoint of a bidirectional inter-process communication 
flow across an Internet Protocol-based computer network--internet.

Enough of Bababa~~ 
So How it happens in python?
import sockets
like making a phone call
'''
import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('wwww.py4inf.com', 80))

'''
Once we have sockets what do we say
HTTP -- HyperText Transport (layer) Protocol
HTTPs
URL -- Uniform Resource Locator: protocal + host + document
Request response cycle: GET and POST
Internet Standards: IETF
Hacking HTTP: open connection, talk to protocol, close
'''
# mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')
# while True:
#     data = mysock.recv(512)
#     if(len(data)< 1):
#         break
#     print(data)
# mysock.close()

'''
Error:
Traceback (most recent call last):
  File "chapter12.py", line 25, in <module>
    mysock.send('GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')
TypeError: a bytes-like object is required, not 'str'
'''
#To solve the problem:

mysock.send(b'GET http://www.py4inf.com/code/romeo.txt HTTP/1.0\n\n')
while True:
    data = mysock.recv(512)
    if(len(data)< 1):
        break
    datas = str(data).split(':')
    for data in datas:
        
        print(data)
mysock.close()

'''
urllib
'''
# import urllib
# fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
# for line in fhand:
#     print (line.strip())
'''
Error:
AttributeError: module 'urllib' has no attribute 'urlopen'
'''
# To Solve

import urllib.request as url
fhand = urllib.urlopen('http://www.py4inf.com/code/romeo.txt')
for line in fhand:
    print (line.strip())

