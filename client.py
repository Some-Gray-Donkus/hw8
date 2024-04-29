#!/usr/bin/env python
# encoding: utf-8

#!/usr/bin/python

import socket, ssl

host = "172.20.255.170"
port = 42702

context = ssl.SSLContext(ssl.PROTOCOL_TLS)
context.verify_mode = ssl.CERT_REQUIRED
context.check_hostname = False
context.load_verify_locations("rootCA.crt")
conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=host)
conn.connect((host, port))

kb = ''

while kb != 'quit':
    kb = input("out: ")
    if kb == 'quit':
        continue
    kb = kb.encode()
    conn.send(kb)
    data = conn.recv(1024)
    data = data.decode()
    print(f"in: {data}")
conn.close()
