# Server 
#

import socket 
import sys
import cmd
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


# TODO account for endianness

class Artemis(cmd.Cmd):

    prompt = "Artemis [>] "
    intro = """    _    ____ _____ _____ __  __ ___ ____  
   / \  |  _ \_   _| ____|  \/  |_ _/ ___| 
  / _ \ | |_) || | |  _| | |\/| || |\___ \ 
 / ___ \|  _ < | | | |___| |  | || | ___) |
/_/   \_\_| \_\|_| |_____|_|  |_|___|____/ 
\nWelcome to Artemis Server"""

    HOST = None
    PORT = 10337
    PROTO = socket.SOCK_STREAM # default is TCP
    BUFFER = 1024
    socket_object = None

    def do_launch(self, arg):
        """ Run the server """
        try:
            self.socket_object = socket.socket(socket.AF_INET, self.PROTO)
        except OSError as msg:
            pass

        if not self.HOST:
            self.HOST = socket.gethostname()

        try:
            print(f"Using settings:\nHOST:  {self.HOST}\nPORT:  {self.PORT}\nPROTO: {self.PROTO}")
            self.socket_object.bind((self.HOST, self.PORT))
            
            if self.PROTO == socket.SOCK_STREAM:    
                self.socket_object.listen()

                while True:
                    connection, client_address = self.socket_object.accept()
                    with connection:
                        print('Connected by', client_address)
                        data = connection.recv(self.BUFFER)
                        if not data: 
                           break
                        connection.send(data)
                        output_be = str(struct.unpack_from('>'+'c'*len(bytearray(data)), bytearray(data))) # decode in BE
                        output_le = str(struct.unpack_from('<'+'c'*len(bytearray(data)), bytearray(data))) # decode in LE
                        print(data)                                
                        print(output_be)
                        print(output_le)


            else:
                while True:
                    data, client_address = self.socket_object.recvfrom(self.BUFFER)
                    print('Connected by', client_address)
                    if data:
                        self.socket_object.sendto(data, client_address)
                        print(data)

        except socket.error as msg:
            print(msg)            
            print('Could not open socket')
            sys.exit(1)

        except KeyboardInterrupt:
            pass

        self.socket_object.close()

    def do_setbuffer(self, arg):
        """ Set the buffer size for the server """
        self.BUFFER = arg

    def do_setport(self, arg):
        """ Set the port for the server """
        self.PORT = arg

    def do_sethost(self, arg):
        """ Set the host (local) IP for the server """
        if not arg:
            self.HOST = socket.gethostname()
        else:
            self.HOST = arg    

    def do_setprotocol(self, arg):
        """ Set protocol to TCP or UDP """
        if arg == "tcp":
            self.PROTO = socket.SOCK_STREAM    
        elif arg == "udp":
            self.PROTO = socket.SOCK_DGRAM        
        else:
            print("Please choose tcp or udp")

    def do_gethostname(self, arg):
        """ Calls socket.gethostname() """
        print(socket.gethostname())                

    def do_settings(self, arg):
        """ Get settings """
        print(f"HOST:  {self.HOST}\nPORT:  {self.PORT}\nPROTO: {self.PROTO}")

    def do_exit(self, arg):
        """ Exit the server """
        exit(0)

    ###################################
    # Help messages
    def help_launch(self):
        print("Run the server")

    def help_setport(self):
            print("Set the port for the server")

    def help_sethost(self):
            print("Set the host (local) IP for the server")

    def help_setprotocol(self):
        print("Set protocol to TCP or UDP [run protocol tcp, or protocol udp]")

    def help_gethostname(self):
            print("Calls socket.gethostname()")

    def help_settings(self):
        print("Get settings")

    def help_exit(self):
            print("Exit the server")

if __name__ == '__main__':
    Artemis().cmdloop()










