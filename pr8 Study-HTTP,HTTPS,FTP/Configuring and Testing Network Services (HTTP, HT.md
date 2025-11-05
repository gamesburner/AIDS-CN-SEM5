## Configuring and Testing Network Services (HTTP, HTTPS, FTP)

This guide provides step-by-step instructions for setting up a server to provide HTTP, HTTPS, and FTP services and testing them from client devices within Cisco Packet Tracer.

### Required Components

* 1 Server
* 1 Switch
* 2 End Devices (PCs)
* Copper Straight-Through Cables


### Step 1: Network Assembly and IP Configuration

First, build the physical network and assign static IP addresses to each device.

1. Place the server, switch, and two PCs into the workspace.
2. Connect the server and both PCs to the switch using **Copper Straight-Through** cables.
3. Assign static IP addresses. Click on each device, navigate to **Desktop > IP Configuration**, and enter the following:
    * **Server:** IP Address `192.168.1.1`, Subnet Mask `255.255.255.0`
    * **PC0:** IP Address `192.168.1.2`, Subnet Mask `255.255.255.0`
    * **PC1:** IP Address `192.168.1.3`, Subnet Mask `255.255.255.0`

### Step 2: Configure and Test HTTP/HTTPS Services

By default, the server in Packet Tracer has HTTP and HTTPS services enabled. This section covers how to verify and test them.

#### Configure the Web Server

1. Click the **Server** and select the **Services** tab.
2. From the service list on the left, click **HTTP**.
3. Ensure that both the **HTTP** and **HTTPS** services are turned **On**.
4. You will see a list of HTML files. You can click `index.html` and then **Edit** to customize the default web page. Save your changes if you make any.

#### Test from a Client Device

1. Click on a PC (e.g., PC0) and open the **Desktop** tab.
2. Select the **Web Browser** application.
3. To test HTTP, enter the server's IP address in the URL bar and press Go.

```
http://192.168.1.1
```

4. To test HTTPS, enter the server's IP address with the HTTPS prefix.

```
https://192.168.1.1
```

5. In both cases, the default web page from the server should be displayed, confirming the services are working.

### Step 3: Configure and Test FTP Service

This section details how to set up an FTP user account on the server and use it to transfer files.

#### Configure the FTP Server

1. On the **Server**, navigate to the **Services** tab and select **FTP**.
2. Ensure the FTP service is turned **On**.
3. In the "User Setup" section, create a new user account:
    * **Username:** `cisco`
    * **Password:** `password`
    * **Permissions:** Check all boxes (Write, Read, Delete, Rename, List).
4. Click **Add** to save the new user.

#### Test FTP File Transfer

First, create a file on one PC to upload to the server.

1. On **PC0**, go to the **Desktop** tab and open the **Text Editor**.
2. Type some text, like "This is a test file."
3. Click **File > Save** and name it `upload.txt`.

Next, use the command prompt to upload the file.

1. On **PC0**, open the **Command Prompt**.
2. Connect to the FTP server.

```
ftp 192.168.1.1
```

3. When prompted, enter the username (`cisco`) and password (`password`) you created.
4. Upload the file using the `put` command.

```
put upload.txt
```

You should see a message confirming the file transfer is complete.

Finally, download the file to the second PC.

1. On **PC1**, open the **Command Prompt**.
2. Connect to the FTP server and log in using the same credentials.

```
ftp 192.168.1.1
```

3. Download the file from the server using the `get` command.

```
get upload.txt
```

4. Close the FTP session by typing `quit`. You can now find the `upload.txt` file on PC1's local file system, confirming the successful transfer.
