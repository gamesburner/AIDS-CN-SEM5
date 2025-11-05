import socket

# Server socket setup
server_socket = socket.socket()
server_socket.bind(('127.0.0.1', 1234))
server_socket.listen(1)
print("Server waiting for connection...")

conn, addr = server_socket.accept()
print("Connected with", addr)

# Receive message from client
msg = conn.recv(1024).decode()
print("Client:", msg)

# Send reply
conn.send("Hello Client, I am Server!".encode())

conn.close()
server_socket.close()