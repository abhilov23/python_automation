#chat client side

import socket 

#define constants to be used
DEST_IP = socket.gethostbyname(socket.gethostname())
DEST_PORT = 12345
ENCODER = "utf-8"
BYTESIZE = 1024

#create a client socket object
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((DEST_IP, DEST_PORT))

#send a message to server
while True:
    message = client_socket.recv(BYTESIZE).decode(ENCODER)
    print(f"Server response: {message}")

    #quit if the server wants to quit (using a quit flag)
    if message == "quit":
        client_socket.send("quit".encode(ENCODER))
        print("Ending the chat\n")
        break
    else:
        print(f"\n{message}")
        message = input("Message:")
        client_socket.send(message.encode(ENCODER))

#close the client socket
client_socket.close()