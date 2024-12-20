#chat server side
import socket

#define constants to be used
HOST_IP = socket.gethostbyname(socket.gethostname())
HOST_PORT = 12345
ENCODER = "utf-8"
BYTESIZE = 1024

#create a socket object, and binding it with ip/port 
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#bind the socket to the host and port
server_socket.bind((HOST_IP, HOST_PORT))
#listen for incoming connections
server_socket.listen()


#Accept any incoming connection and let them know that they are connected
print("Server is running......\n")
client_socket, client_address = server_socket.accept()
client_socket.send("you are connected to the server.....\n".encode(ENCODER))
print(f"Connected with client: {client_address}\n")

#send/receive messages
while True:
    #receive message from client
    message = client_socket.recv(BYTESIZE).decode(ENCODER)
    #quit if the client side want to quit, else display the message
    if message == "quit":
        client_socket.send("bye bye...".encode(ENCODER))
        print("\n client disconnected")
        break
    else:
        print(f"\n {message}")
        message = input("Message:")
        client_socket.send(message.encode(ENCODER))

#close the socket
server_socket.close()