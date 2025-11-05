## Configuring a 3-Router Network with RIP Protocol

This guide outlines the procedure for building and configuring a network with three routers using the Routing Information Protocol (RIP) in Cisco Packet Tracer. This setup enables communication between devices across different local networks.

### Required Components

* 3 Routers (e.g., 4331 model)
* 3 Switches (e.g., 2960 model)
* 6 PCs
* Appropriate cables (Copper Straight-Through and Serial DTE/DCE)


### Step 1: Assemble the Network Topology

1. Place all the routers, switches, and PCs in the workspace.
2. For each router, you must add serial interfaces. Click a router, go to the **Physical** tab, turn it off, drag the **NIM-2T** module into an available slot, and turn the router back on. Repeat for all three routers.
3. Connect the devices as follows:
    * Connect two PCs to each switch using **Copper Straight-Through** cables.
    * Connect each switch to its corresponding router's GigabitEthernet interface (e.g., `GigabitEthernet0/0/0`).
    * Connect the routers to each other using **Serial DCE** cables. For instance, connect Router0 (`Serial0/1/0`) to Router1 (`Serial0/1/0`), and Router1 (`Serial0/1/1`) to Router2 (`Serial0/1/0`). Note which end of the cable has the clock symbol, as this is the DCE side that requires a `clock rate` command.

### Step 2: Plan and Assign IP Addresses

Organize your network into distinct subnets. Below is an example addressing scheme:

* **LAN 1 (Router0):** Network `192.168.1.0 /24`
* **LAN 2 (Router1):** Network `192.168.2.0 /24`
* **LAN 3 (Router2):** Network `192.168.3.0 /24`
* **WAN Link 1 (Router0-Router1):** Network `10.0.0.0 /30`
* **WAN Link 2 (Router1-Router2):** Network `20.0.0.0 /30`

Configure the IP addresses on the PCs. For each PC, navigate to **Desktop > IP Configuration**.

* **PCs on LAN 1:** Assign IPs like `192.168.1.2`, `192.168.1.3`. Set their **Default Gateway** to `192.168.1.1`.
* **PCs on LAN 2:** Assign IPs like `192.168.2.2`, `192.168.2.3`. Set their **Default Gateway** to `192.168.2.1`.
* **PCs on LAN 3:** Assign IPs like `192.168.3.2`, `192.168.3.3`. Set their **Default Gateway** to `192.168.3.1`.


### Step 3: Configure Router Interfaces

Access the **CLI** for each router and configure its interfaces.

#### Router0 Configuration

```
enable
configure terminal
! Configure LAN Interface
interface GigabitEthernet0/0/0
 ip address 192.168.1.1 255.255.255.0
 no shutdown
! Configure WAN Interface to Router1
interface Serial0/1/0
 ip address 10.0.0.1 255.255.255.252
 clock rate 64000
 no shutdown
exit
```


#### Router1 Configuration

```
enable
configure terminal
! Configure LAN Interface
interface GigabitEthernet0/0/0
 ip address 192.168.2.1 255.255.255.0
 no shutdown
! Configure WAN Interface to Router0
interface Serial0/1/0
 ip address 10.0.0.2 255.255.255.252
 no shutdown
! Configure WAN Interface to Router2
interface Serial0/1/1
 ip address 20.0.0.1 255.255.255.252
 clock rate 64000
 no shutdown
exit
```


#### Router2 Configuration

```
enable
configure terminal
! Configure LAN Interface
interface GigabitEthernet0/0/0
 ip address 192.168.3.1 255.255.255.0
 no shutdown
! Configure WAN Interface to Router1
interface Serial0/1/0
 ip address 20.0.0.2 255.255.255.252
 no shutdown
exit
```

The `no shutdown` command activates the interfaces, turning the link status indicators from red to green.

### Step 4: Configure RIP Routing Protocol

Enable RIP on each router so they can share routing information. You only need to advertise the directly connected networks.

#### Router0 RIP Configuration

```
configure terminal
router rip
version 2
network 192.168.1.0
network 10.0.0.0
end
```


#### Router1 RIP Configuration

```
configure terminal
router rip
version 2
network 192.168.2.0
network 10.0.0.0
network 20.0.0.0
end
```


#### Router2 RIP Configuration

```
configure terminal
router rip
version 2
network 192.168.3.0
network 20.0.0.0
end
```


### Step 5: Verify Connectivity

After configuring RIP, wait a moment for the routers to exchange routing tables.

1. **Check Routing Tables:** On any router, use the `show ip route` command in privileged exec mode (`Router#`) to see the routes learned via RIP (indicated by an "R").
2. **Test End-to-End Connectivity:** Open the Command Prompt on a PC in one network (e.g., PC on LAN 1 with IP `192.168.1.2`) and ping a PC in a different network (e.g., PC on LAN 3 with IP `192.168.3.2`).

```
ping 192.168.3.2
```


A successful series of replies confirms that RIP is working correctly and your multi-router network is fully configured.

