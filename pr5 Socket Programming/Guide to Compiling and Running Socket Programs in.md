## Guide to Compiling and Running Socket Programs in Java

This guide details the process of compiling and running basic client-server applications for both TCP and UDP protocols using Java. You will need four source code files to complete this process.

### Required Source Files

Your project is composed of four essential Java files that facilitate client-server communication:

* `TCPServer.java`: This program creates a server that listens for connection requests from clients over TCP.
* `TCPClient.java`: This program initiates a connection to the TCP server to exchange data.
* `UDPServer.java`: This program listens for connectionless datagram packets sent via UDP.
* `UDPClient.java`: This program sends datagram packets to the UDP server.


### Step 1: Compile the Java Files

First, you must compile the human-readable `.java` source files into executable `.class` files containing Java bytecode. This is accomplished using the `javac` command.

1. Open a terminal or command prompt.
2. Navigate to the directory containing your four `.java` files.
3. Compile each file by running the following commands:

```
javac TCPServer.java
javac TCPClient.java
javac UDPServer.java
javac UDPClient.java
```

Upon successful compilation, a corresponding `.class` file will be generated for each source file in the same directory.

### Step 2: Execute the Client-Server Programs

To run the applications, you will need **two** separate terminal windows: one for the server and one for the client. It is crucial to **run the server file first** so it can listen for the client's connection.

#### Running the TCP Application

1. **Terminal 1 (Server):** Start the TCP server program. It will wait for a client to connect.

```
java TCPServer
```

2. **Terminal 2 (Client):** In a new terminal window, run the TCP client program. It will attempt to establish a connection with the running server.

```
java TCPClient
```


#### Running the UDP Application

The execution order for the UDP application is the same as for TCP.

1. **Terminal 1 (Server):** Start the UDP server. It will begin listening for incoming data packets.

```
java UDPServer
```

2. **Terminal 2 (Client):** In a second terminal, run the UDP client to send a packet to the server.

```
java UDPClient
```

