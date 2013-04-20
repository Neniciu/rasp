#!/usr/bin/python           
# TCP server. Runs on the Raspberry Pi.

import socket               # Import socket module
s = socket.socket()         # Create a socket object
host = '10.10.0.30'     # Get local machine name
port = 10974               # Reserve a port for your service.

print 'Server started!'
print 'Waiting for clients...'

s.bind((host, port))        # Bind to the port
s.listen(5)                 # Now wait for client connection.
c, addr = s.accept()     # Establish connection with client.
print 'Got connection from', addr
while True:
   msg = c.recv(2) # get 2 bytes from the TCP connection
   write(msg)  # write the 2 bytes to the serial interface
