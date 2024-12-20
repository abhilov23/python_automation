#UDP client side
import socket

#create a UDP ipv4 
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

#send data via connectionless protocol using sendto function
client_socket.sendto("hello darling, I love you!".encode("utf-8"),(socket.gethostbyname(socket.gethostname()), 12345))
