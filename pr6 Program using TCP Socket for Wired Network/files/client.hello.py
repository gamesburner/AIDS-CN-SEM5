import socket

# Client socket setup
client_socket = socket.socket()
client_socket.connect(('127.0.0.1', 1234))

# Send hello to server
client_socket.send("Hello Server, I am Client!".encode())

# Receive reply
msg = client_socket.recv(1024).decode()
print("Server:", msg)

client_socket.close()