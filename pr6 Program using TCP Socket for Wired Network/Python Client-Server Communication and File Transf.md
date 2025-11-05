## Python Client-Server Communication and File Transfer

This guide explains how to execute a Python-based client-server application designed to perform an initial handshake and transfer a file.

### Core Components

Your application requires five files to be placed in the same directory:

* `server.py`: The main server script that listens for incoming connections.
* `client.py`: The main client script that connects to the server.
* `server.hello.py`: A helper module used by the server to handle the initial "Hello" greeting.
* `client.hello.py`: A helper module used by the client to respond to the server's greeting.
* `sample.txt`: A text file located in the server's directory that will be transferred to the client.


### Execution Guide

To run the application, you need two terminal windows to manage the **server** and **client** processes independently. The server must be started first.

#### Step 1: Start the Server

1. Open your first terminal window.
2. Navigate to the directory where you have saved all five files.
3. Execute the server script using the following command. The server will start and wait for a client to connect.

```
python server.py
```


#### Step 2: Run the Client

1. Open a second, separate terminal window.
2. Navigate to the same project directory.
3. Execute the client script to initiate the connection to the server.

```
python client.py
```


### Process Overview

Once the client connects to the server, the following actions occur automatically:

1. **Handshake:** The server and client exchange "Hello" messages. This initial communication is managed by the logic within the `server.hello.py` and `client.hello.py` modules, confirming that a stable connection is established.
2. **File Transfer:** After the successful handshake, the server reads the contents of `sample.txt` and transmits the data to the client. The client receives this data and saves it, effectively transferring the file.
3. **Verification:** You can confirm the process was successful by observing the "Hello" messages printed in both terminals and by finding a newly created `sample.txt` file in the same directory, which is the copy received by the client.
