import socket

# Create TCP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind to localhost and port
HOST = '127.0.0.1'
PORT = 12345
server_socket.bind((HOST, PORT))

# Start listening
server_socket.listen(1)
print(f"Server started. Waiting for connection on {HOST}:{PORT}...")

# Accept connection
conn, addr = server_socket.accept()
print(f"Connected with client: {addr}")

# Part A: Say Hello
msg = conn.recv(1024).decode()
print("Client says:", msg)
conn.send("Hello Client! Nice to meet you.".encode())

# Part B: File Transfer
filename = "sample.txt"
with open(filename, "rb") as f:
    data = f.read()
    conn.sendall(data)

print(f"File '{filename}' sent successfully!")

# Close connection
conn.close()
server_socket.close()