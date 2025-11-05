import socket

# Create TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server (localhost)
HOST = '127.0.0.1'
PORT = 12345
client_socket.connect((HOST, PORT))

# Part A: Say Hello
client_socket.send("Hello Server!".encode())
msg = client_socket.recv(1024).decode()
print("Server says:", msg)

# Part B: Receive File
filename = "received.txt"
with open(filename, "wb") as f:
    data = client_socket.recv(1024)
    while data:
        f.write(data)
        data = client_socket.recv(1024)

print(f"File received successfully and saved as '{filename}'")

# Close socket
client_socket.close()