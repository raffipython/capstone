# Client
# 

import socket
import sys
import struct

# socket()
# gethostname()
# close()
# bind()
#
#  listen()
#  accept()
#  connect()
#  recv()
#  send()
#
#  sendto()
#  recvfrom()


HOST = "ubuntu"
PORT = 10337
PROTO = sys.argv[1]
BUFFER = 1024
socket_object = None

message = b"ABCD"

try:
    if PROTO == "tcp":

        socket_object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket_object.connect((HOST, PORT))
            
        socket_object.send(message)
        data = socket_object.recv(BUFFER)

        #https://developer.opto22.com/pythonmmp/codesamples/
        output_be = str(struct.unpack_from('>'+'c'*len(bytearray(data)), bytearray(data))) # decode in BE
        output_le = str(struct.unpack_from('<'+'c'*len(bytearray(data)), bytearray(data))) # decode in LE

        print(data)
        print(output_be)
        print(output_le)


        socket_object.close()

    else:
        socket_object = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        socket_object.sendto(message, (HOST, PORT))
        data = socket_object.recvfrom(1024)



except OSError as msg:
    print(msg)
    socket_object.close()
    print('Could not open socket')
    sys.exit(1)
