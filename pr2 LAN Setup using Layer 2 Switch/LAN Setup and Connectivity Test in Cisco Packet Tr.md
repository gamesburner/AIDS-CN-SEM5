## LAN Setup and Connectivity Test in Cisco Packet Tracer

This guide details how to create a simple Local Area Network (LAN) using a Layer 2 switch and two end devices in Cisco Packet Tracer, and how to verify connectivity between them.

### Required Components

* 1 Switch (e.g., 2960 model)
* 2 End Devices (e.g., PCs)
* 2 Copper Straight-Through Cables


### Step 1: Assemble the Network Topology

1. Launch the Cisco Packet Tracer application.
2. From the device selection box, add one **Switch** and two **PCs** to the logical workspace.
3. Select the **Connections** icon (lightning bolt), choose the **Copper Straight-Through** cable, and connect each PC to a separate port on the switch.
    * Connect PC0 (FastEthernet0) to Switch (FastEthernet0/1).
    * Connect PC1 (FastEthernet0) to Switch (FastEthernet0/2).

### Step 2: Configure IP Addresses

You must assign a unique IP address to each PC to enable communication.

1. Click on the first PC (PC0).
2. Navigate to the **Desktop** tab and select **IP Configuration**.
3. Enter the following details:
    * **IP Address:** 192.168.1.1
    * **Subnet Mask:** 255.255.255.0
4. Close the IP Configuration window.
5. Repeat the process for the second PC (PC1), ensuring you assign a different IP address within the same network.
    * **IP Address:** 192.168.1.2
    * **Subnet Mask:** 255.255.255.0

### Step 3: Verify Network Connectivity

The `ping` command sends test packets to a target device to check if it is reachable.

1. Open an end device (e.g., PC0).
2. Navigate to the **Desktop** tab and open the **Command Prompt**.
3. Type the `ping` command followed by the IP address of the other PC (PC1).

```
ping 192.168.1.2
```

4. Press Enter to execute the command. A successful connection will result in four reply messages from the destination IP address, confirming that your network is correctly configured.
