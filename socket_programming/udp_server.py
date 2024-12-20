#UDP server side
import socket

#create a server side socket IPV4 and UDP (SOCK_DGRAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#bind the server socket to a specific IP and port
server_socket.bind((socket.gethostbyname(socket.gethostname()), 12345))

#here you do not listen from anyone because UDP is a connectionless protocol


#receive data from client, instead of recv() we are using recvfrom() method.
message, client_address = server_socket.recvfrom(1024)
print(message.decode("utf-8"))
print(client_address)
