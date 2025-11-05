## Combined Wired and Wireless LAN Setup in Cisco Packet Tracer

This guide explains how to build a network that includes both wired and wireless devices connected through a central router in Cisco Packet Tracer.

### Required Components

* 1 Router (e.g., 4331 model)
* 1 Switch (e.g., 2960 model)
* 1 Access Point (AP)
* 2 PCs
* 1 Laptop
* 1 Smartphone


### Step 1: Assemble the Network Topology

1. Add all the required devices to the workspace.
2. Use **Copper Straight-Through** cables to make the following wired connections:
    * Connect the Router (e.g., GigabitEthernet0/0/0) to the Switch (e.g., GigabitEthernet0/1).
    * Connect the Switch (e.g., FastEthernet0/1) to PC0.
    * Connect the Switch (e.g., FastEthernet0/2) to PC1.
    * Connect the Router (e.g., GigabitEthernet0/0/1) to the Access Point (Port 0).

### Step 2: Configure the Router

The router will act as the default gateway, directing traffic between devices.

1. Click the Router and go to the **CLI** (Command-Line Interface) tab.
2. Enter the following commands to configure the interface connected to the switch and enable it. This interface will serve the wired and wireless LANs.

```
enable
configure terminal
interface GigabitEthernet0/0/0
ip address 192.168.1.1 255.255.255.0
no shutdown
exit
```


### Step 3: Configure the Wireless Access Point

Set up the AP to create a wireless network.

1. Click the Access Point and open the **Config** tab.
2. Select the **Port 1** interface from the left-hand menu.
3. Set a custom **SSID** (the network name), for example, `MyCorpWiFi`.
4. For authentication, select **WEP** and enter a 10-digit key (e.g., `1234567890`).

### Step 4: Configure End Devices

Assign IP addresses to all PCs, the laptop, and the smartphone so they can communicate.

#### Wired PCs (PC0 and PC1)

1. Click on PC0, go to the **Desktop** tab, and select **IP Configuration**.
2. Set the configuration as follows:
    * **IP Address:** 192.168.1.2
    * **Subnet Mask:** 255.255.255.0
    * **Default Gateway:** 192.168.1.1 (the router's IP address)
3. Repeat for PC1 using a unique IP address (e.g., `192.168.1.3`).

#### Wireless Devices (Laptop and Smartphone)

1. **For the Laptop:** You must first install a wireless module. Click the Laptop, go to the **Physical** tab, turn it off using the power button, drag the default Ethernet module out, and drag a wireless module (e.g., WPC300N) in. Turn the laptop back on.
2. Click on the Laptop, go to the **Desktop** tab, and select **PC Wireless**.
3. Navigate to the **Connect** tab, wait for the SSID `MyCorpWiFi` to appear, select it, and click **Connect**.
4. Enter the WEP key (`1234567890`) when prompted.
5. Once connected, go back to the **Desktop** tab and open **IP Configuration**. Set the device to use **DHCP** or configure it statically with a unique IP (e.g., `192.168.1.4`) and the Default Gateway `192.168.1.1`.
6. Repeat the connection and IP configuration steps for the Smartphone.

### Step 5: Verify Connectivity

Use the `ping` command to test communication between different parts of your network.

* **Test internal connectivity:** Open the Command Prompt on PC0 and ping the laptop.

```
ping 192.168.1.4 
```

* **Test gateway connectivity:** From any end device, ping the router's IP address.

```
ping 192.168.1.1
```


Successful replies indicate that your wired and wireless devices are correctly configured and can communicate through the router.

