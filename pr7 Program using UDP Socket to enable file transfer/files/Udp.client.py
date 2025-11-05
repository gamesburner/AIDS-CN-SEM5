import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('127.0.0.1', 9999)

# Function to send file
def send_file(filename):
    with open(filename, "rb") as f:
        data = f.read(1024)
        while data:
            client_socket.sendto(data, server_address)
            data = f.read(1024)
        client_socket.sendto(b"EOF", server_address)
    print(f"{filename} sent successfully!")

# Send Script File
send_file("script.py")

# Send Text File
send_file("text.txt")

# Send Audio File
send_file("audio.mp3")

# Send Video File
send_file("video.mp4")

client_socket.close()