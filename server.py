#!/usr/bin/env python
# encoding: utf-8

#!/usr/bin/python

import socket, ssl

port = 42702

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.load_cert_chain(certfile = "server2.crt", keyfile = "serverVM.key")
with context.wrap_socket(socket.socket(socket.AF_INET), server_side = True) as connstream:

    connstream.bind(('', port))
    connstream.listen()

    conn, addr = connstream.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            if not data:
                break
            conn.sendall(data)
        conn.close()
