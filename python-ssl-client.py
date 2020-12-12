#!/usr/bin/python3
import socket
import ssl
server_name = 'mypocketxp.com'
server_port = 110
context = ssl.create_default_context()
context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
context.load_verify_locations("/etc/ssl/certs/DST_Root_CA_X3.pem")
conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=server_name)
conn.connect((server_name, server_port))
conn.send(b"Hello, world!\n")
conn.close()
