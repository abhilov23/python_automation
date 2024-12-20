#TCP server side
import socket 

#create a server side socket using IPV4 (AF_INET) and TCP (sock_stream)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#see how to get IP address dynamically 
print(socket.gethostname()) #printing the hostname

#printing the IP address of the system via hostname
print(socket.gethostbyname(socket.gethostname())) 

#bind our new socket to a tuple using bind fn:  socket.bind(IP address, Port Address)
server_socket.bind((socket.gethostbyname(socket.gethostname()), 12345))

#put the socket into listening mode to listen for any possible connections
server_socket.listen()

#now we want to listen it contineously to accept connections using accept() method
#and for that we are also using a while loop
while True:
    #we are getting the information about the socket that is connected in client_socket
    #and client_address in client_address
    client_socket, client_address = server_socket.accept()
    print(type(client_socket)) #printing the type of message in client_socket
    print(client_socket) #printing the client_socket data
    print(type(client_socket)) #printing the type of client_socket 
    print(client_address) #printing the client_address
    print(f"Client connected with address: {client_socket.getpeername()}") #brings you the ipaddress and portname of the same

    #send a message to the client that just connected, but we cannot send
    #string directly so we need to encode it via internet
    client_socket.send("Hello from server!".encode("utf-8"))

    #close the connection with the client
    server_socket.close()
    break #to break out of the loop after one connection