#tcp client side 
import socket 


#creating a client side IPV4 socket (AF_INET) and TCP (sock_stream)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#in our server socket all we did was to bind it with the system IPnd
# TCP then start listening to the incoming connections on any port 
# but not with the client socket, here we need to send a connection to a 
#specific server, like our server socket.

#we are going to use connect() method for connection socket.connect(IP, port_number)
client_socket.connect((socket.gethostbyname(socket.gethostname()),12345))

#receiving the method from the server using recv method
#also you need to specify the maximum number of bytes to receive
message = client_socket.recv(1024)
print(message.decode("utf-8"))
print(type(message)) #to check the data bytes in the computer side

#close the client socket
client_socket.close()