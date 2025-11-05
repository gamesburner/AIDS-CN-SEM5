## Configuring a DHCP Server in Cisco Packet Tracer

This guide provides a comprehensive walkthrough for setting up a DHCP server to automatically assign IP addresses to client machines in a simple network.

### Required Components

* 1 Server
* 1 Switch (2960 model)
* 2 PCs
* Copper Straight-Through Cables


### Step 1: Build the Network Topology

First, assemble the network by placing and connecting the required devices in the workspace.

1. Add the Server, Switch, and two PCs to the workspace.
2. Select the **Connections** icon (lightning bolt) and choose the **Copper Straight-Through** cable.
3. Connect the devices in the following order:
    * Connect the **Server** (FastEthernet0) to the **Switch** (FastEthernet0/1).
    * Connect **PC0** (FastEthernet0) to the **Switch** (FastEthernet0/2).
    * Connect **PC1** (FastEthernet0) to the **Switch** (FastEthernet0/3).
4. Wait for the connection lights on the switch ports to turn green, indicating an active link.

### Step 2: Assign a Static IP Address to the Server

The DHCP server needs a fixed, unchanging IP address so that clients can always find it.

1. Click on the **Server** device to open its configuration window.
2. Navigate to the **Desktop** tab and select **IP Configuration**.
3. Ensure the **Static** option is selected.
4. Enter the following information:
    * **IP Address:** `192.168.1.1`
    * **Subnet Mask:** `255.255.255.0`
    * **Default Gateway:** `192.168.1.1`
5. Close the IP Configuration window.

### Step 3: Configure the DHCP Service

Next, configure the server to lease IP addresses to clients from a defined address pool.

1. On the **Server**, select the **Services** tab.
2. From the service list on the left, choose **DHCP**.
3. Turn the DHCP **Service** to **On**.
4. Configure the `serverPool` with the following settings:
    * **Default Gateway:** `192.168.1.1`
    * **DNS Server:** `192.168.1.1`
    * **Start IP Address:** `192.168.1.10` (This prevents conflicts with the server's static IP).
    * **Subnet Mask:** `255.255.255.0`
    * **Maximum Number of Users:** `50`
5. Click the **Save** button to apply the changes to the pool.

### Step 4: Configure PCs to Use DHCP

Finally, set the client PCs to request their IP configuration automatically from the server.

1. Click on **PC0**, go to the **Desktop** tab, and open **IP Configuration**.
2. Select the **DHCP** radio button.
3. The PC will broadcast a DHCP request, and after a moment, the fields will auto-populate. You should see it has received an IP address like `192.168.1.10`.
4. Close the window for PC0 and repeat the same steps for **PC1**. It will receive the next available IP address, `192.168.1.11`.
