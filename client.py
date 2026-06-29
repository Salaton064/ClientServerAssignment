import socket

HOST = "127.0.0.1"      # Local computer
PORT = 5000             # Same port as the server

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

message = "Hello Server!"

client.send(message.encode())

reply = client.recv(1024).decode()

print("Server says:", reply)

client.close()