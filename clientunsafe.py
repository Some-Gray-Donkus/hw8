#!/usr/bin/env python
# encoding: utf-8

#!/usr/bin/python

import socket

host = "172.20.255.170"
port = 42702

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((host, port))

kb = ''

while kb != 'quit':
    kb = input("out: ")
    if kb == 'quit':
        continue
    kb = kb.encode()
    s.send(kb)
    data = s.recv(1024)
    data = data.decode()
    print(f"in: {data}")
s.close()
