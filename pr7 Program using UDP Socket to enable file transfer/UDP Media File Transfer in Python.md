## UDP Media File Transfer in Python

This guide details how to execute a UDP-based client-server application in Python to transfer various media files from a server to a client.

### Required Files

For this process, ensure the following files are located in your project directory. The media files must be in the same folder as the `udp.server.py` script.

#### Main Scripts

* `udp.server.py`: The server script responsible for listening for client requests and sending files.
* `udp.client.py`: The client script that connects to the server to receive files.


#### Files for Transfer

* `audio.mp3`
* `video.mp4`
* `script.py`
* `text.txt`


### Execution Steps

The server must be running before the client can connect. You will need two separate command prompt or terminal windows.

#### Step 1: Start the UDP Server

1. Open a terminal and navigate to the directory containing your files.
2. Run the server script. It will start listening for incoming datagrams from a client.

```
python udp.server.py
```


#### Step 2: Run the UDP Client

1. In a second terminal window, navigate to the same directory.
2. Execute the client script to initiate the file transfer process.

```
python udp.client.py
```


### Transfer and Verification

Once the client is running, it will communicate with the server to receive the designated files. The transfer process is verified by checking the client's directory after the script finishes.

* **File Renaming:** To distinguish transferred files from original ones, the client will automatically rename each file it receives by adding the prefix `received_` to the original filename.
* **Verification:** After the transfer is complete, you should find the following new files in your directory:
    * `received_audio.mp3`
    * `received_video.mp4`
    * `received_script.py`
    * `received_text.txt`

The presence of these renamed files confirms a successful transfer.

