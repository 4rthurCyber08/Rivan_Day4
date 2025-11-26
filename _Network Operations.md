
<!-- Your monitor number = #$34T# -->


## ⛅ Warm Up for Day 4.

### 🔧 Configure the following:
  - Switch (__CoreTAAS__ & __CoreBABA__)
  - Voice Gateway/Call Manager (__CUCM - Cisco Unified Call Manager__)
  - Router (__EDGE__)

<br>

Verify:

~~~cmd
@cmd
ping 10.#$34T#.1.10             PC Network Adapter
ping 10.#$34T#.1.2		    CoreTAAS
ping 10.#$34T#.1.4		    CoreBABA
ping 10.#$34T#.100.8		CUCM
ping 10.#$34T#.#$34T#.1		EDGE - INSIDE
ping 200.0.0.#$34T#		    EDGE - OUTSIDE

ping 200.0.0.k		        Klassmate's EDGE	       k = klassmate's Monitor Number
ping 10.k.100.8		        Klassmate's CUCM
ping 10.k.1.4		        Klassmate's CoreBABA
ping 10.k.1.2		        Klassmate's CoreTAAS
ping 10.k.1.10		        Klassmate's PC
~~~

Your Branch must be able to call other klassmates  

<br>

View your cameras:
  - http://10.#$34T#.50.6  
  - http://10.#$34T#.50.8  

<br>
<br>

---
&nbsp;

## OSI Model 
Interpret and Explain the OSI Model

### Layer 1:
Speed is measured in bits, while data is measured in Bytes

### Layer 2:
MAC Address: OUI | NIC
Switching "How Switches Forward Packets"

@Linux
arp -a

@Windows
arp -a

@Cisco
arp -a

Broadcast Storm
- STP 802.1d
- - RSTP 802.1w
  - Port Security
 
- L3
  - Routing
  - IP Packet Filtering
 
- L4
  - Open Ports
  - FTP
  - HTTP
  - DNS
  - Chargen

- L5
  - RTP
  - TCP/UDP
  - SPAN (Port Mirror)
  
- L6
  - Stegheide
  - Alternate Data Stream

- L7
  - NetFlow

OSI vs TCP/IP Model

L7,L6,L5 = Application Layer
L4 = Transport Layer
L3 = Network Layer
L2, L1 = Data Link Layer




<br>
<br>

---
&nbsp;

## Routing
*How do network devices forward IP packets? *
~~~
!@CoreTAAS
conf t
 ip routing
 int fa0/9
  no switchport
  ip add 10.#$34T#.69.69 255.255.255.248
  no shut
  end
~~~

<br>

~~~
!@CoreBABA
conf t
 ip routing
 int fa0/9
  no switchport
  ip add 10.#$34T#.69.72 255.255.255.248
  no shut
  end
~~~

<br>

Will they ping?
~~~
!@CoreTAAS
ping 10.#$34T#.69.72
~~~

&nbsp;
---
&nbsp;

### Network Engineer: Job Interview Questions for L1/L2 NOC-MSP postions.
*What is a Routing Table?*
*Interpret the components of routing table?*

A routing table is a database, aka a FIB (Forward Information Base), that is used by network devices to efficiently make L3 forwarding decisions.

Palo Alto
| Destination | Next Hop | Metric | Weight | Flags | Age | Interface   |
| ---         | ---      | ---    | ---    | ---   | --- | ---         |
| 0.0.0.0/0   | 0.0.0.0  | 1      |        | A S   |     | ethernet1/1 |

<br>

Fortinet
| Type   | Network  | Gateway IP | Interfaces  | Distance | Metric | Up Since     |
| ---    | ---      | ---        | ---         | ---      | ---    | ---          |
| Static | 0.0.0.0  | 10.0.0.1   | ethernet1/1 | 1        | 0      | 11 hours ago |

<br>

Juniper
| Destination | Type | RtRef | Next hop | Type Index | NhRef | Netif |
| ---         | ---  | ---   | ---      | ---        | ---   | ---   |
| 0.0.0.0/32  | perm | 0     |          | dscd       | 34    | 1     |

<br>

Cisco
~~~
!@CoreTAAS
show ip route
~~~

<br>

Windows
~~~
!@cmd
route print
~~~

<br>

Linux & Windows
~~~
!@terminal
netstat -rn
~~~

## Static Routing
Remove routing to learn
~~~
!@CoreBABA, CUCM, EDGE   (via Serial Connection)
conf t
 no ip routing
 ip routing
 end
~~~

<br>

Syntax:
`ip route [Destination IP]  [Network/Host Mask]  [Exit Interface / Nex-hop]`

<br>

What is a next-hop?

<br>

~~~
!@cmd
tracert 8.8.8.8

Tracing route to 8.8.8.8 over a maximum of 30 hops
  1     2 ms     1 ms     1 ms  192.168.1.1
  2     5 ms     6 ms     5 ms  100.83.0.1
  3     6 ms    11 ms     7 ms  122.2.203.6
  4    12 ms     6 ms     7 ms  210.213.130.15
  5    66 ms    62 ms    49 ms  142.250.175.196
  6     6 ms     6 ms     6 ms  142.251.251.47
  7     8 ms     5 ms     7 ms  142.250.58.243
  8     6 ms    10 ms    10 ms  8.8.8.8
~~~

<br>

Next-hop = 

&nbsp;
---
&nbsp;

### Task 01: Configure static routing on EDGE
To CoreBABA:VLAN 10
~~~
!@EDGE
conf t
 ip route 10.#$34T#.10.4 255.255.255.255 10.#$34T#.#$34T#.4
 end
~~~

<br>

To CoreBABA:VLAN 100
~~~
!@EDGE
conf t
 ip route 10.#$34T#.100.4  255.255.255.255  ___.___.___.___
 end
~~~

<br>

To CUCM
~~~
!@EDGE
conf t
 ip route 10.#$34T#.100.___  255.255.255.255 ___.___.___.___
 end
~~~

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

&nbsp;
---
&nbsp;

### ANSWER

<details>
<summary>Show Answer</summary>
  
Do not forget the return traffic.  
From CUCM to EDGE
~~~
!@CUCM
conf t
 ip route 10.#$34T#.#$34T#.1  255.255.255.255 10.#$34T#.100.4
 end
~~~

</details>

&nbsp;
---
&nbsp;

### Host Route vs Network Route
### 🎯 Exercise 01: Review. Find the network of the following IP addresses:
| Network          | Host IP           |
| ---              | ---               |
|                  | 10.1.100.79 /18   |
|                  | 172.16.145.18 /20 |
|                  | 192.168.1.205 /30 | 

<br>
<br>

&nbsp;
---
&nbsp;

### ANSWER

<details>
<summary>Show Answer</summary>
	
| Network           | Host IP           |
| ---               | ---               |
| 10.1.64.0 /18     | 10.1.100.79 /18   |
| 172.16.144.0 /20  | 172.16.145.18 /20 |
| 192.168.1.204 /30 | 192.168.1.205 /30 | 
 
</details>

&nbsp;
---
&nbsp;

### Task 02: Configure a static network route on EDGE destined for all VLANs
~~~
!@EDGE
conf t
 ip route 10.#$34T#.0.0  255.255.0.0  10.#$34T#.#$34T#.4
~~~

<br>

Static route on windows
~~~
!@cmd
route add 10.0.0.0 mask 255.0.0.0 10.#$34T#.1.4 -p
route add 200.0.0.0 mask 255.255.255.0 10.#$34T#.1.4 -p
~~~

<br>
<br>

---
&nbsp;

### Exercise 01: Establish connectivity between the loopback 1 IP of EDGE and the loopback 25 IP of CoreTAAS
- EDGE loop1 (#$34T#.0.0.1/32)
- CoreTAAS loop25 (10.#$34T#.25.25/32)
~~~
!@CoreTAAS
conf t
 ip routing
 int loopback 25
  ip add 10.#$34T#.25.25 255.255.255.255
  end
~~~

<br>

~~~
!@EDGE
conf t
 ip routing
 int loopback 1
  ip add #$34T#.0.0.1 255.255.255.255
  end
~~~

<br>
<br>

Verify - Make sure both CoreTAAS & EDGE can ping each other's loopback interface.
~~~
!@CoreTAAS
ping #$34T#.0.0.1
~~~

<br>

~~~
!@EDGE
ping 10.#$34T#.25.25
~~~

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

&nbsp;
---
&nbsp;

### ANSWER

<details>
<summary>Show Answer</summary>

~~~
!@CoreTAAS
conf t
 ip route #$34T#.0.0.1 255.255.255.255 10.#$34T#.1.4
 end
~~~

<br>

~~~
!@EDGE
conf t
 ip route 10.#$34T#.25.25 255.255.255.255 10.#$34T#.#$34T#.4
 end
~~~

<br>

Every device on path must know how to reach both destinations.
~~~
!@CoreBABA
conf t
 ip route 10.#$34T#.25.25 255.255.255.255 10.#$34T#.1.2
 ip route #$34T#.0.0.1 255.255.255.255 10.#$34T#.#$34T#.4
 end
~~~

</details>

<br>
<br>

---
&nbsp;

## 🔀 Dynamic Routing
*What are the different dynamic routing protocols?*

1. IGP (Interior Gateway Protocol)
  - Link-state - __OSPF__ & __ISIS__
  - Distance Vector - __EIGRP__ & __RIP__

2. EGP (Exterior Gateway Protocol)
  - __BGP__ (Border Gateway Protocol)

<br>
<br>

## 🔀 EIGRP
Steps in configuring EIGRP
1. Decide on an ASN
2. Determine Connected Networks
3. Advertise

~~~
!@CoreBABA
conf t
 int loopback 90
  ip add 10.#$34T#.90.4 255.255.255.240
  exit
 router eigrp 100
  network 10.#$34T#.90.0 0.0.0.15
  network 10.#$34T#.1.0 0.0.0.255
  network 10.#$34T#.10.0 0.0.0.255
  network 10.#$34T#.50.0 0.0.0.255
  network 10.#$34T#.100.0 0.0.0.255
  end
~~~

<br>

~~~
!@CUCM
conf t
 int loopback 90
  ip add 10.#$34T#.90.90 255.255.255.240
  exit
 router eigrp 100
  network 10.#$34T#.90.80 0.0.0.15
  network 10.#$34T#.100.0 0.0.0.255
  end
~~~

&nbsp;
---
&nbsp;

### EIGRP Database
1. __`show ip eigrp neighbors`__ : Neighbor Table
2. __`show ip eigrp interfaces`__ : Interface Table
3. __`show ip eigrp topology`__ : Topology Table

<br>
<br>

## Path Selection Process : Admin Distance & Metric Cost
1. __Longest Prefix Match (LPM)__  
2. __Administrative Distance__
3. __Metric Cost__

~~~
!@CUCM
show ip route
~~~

<br>

| Legend | Routing Protocol | Administrative Distance | Metric |
| ---    | ---              | ---                     | ---    |
| C      | Connected        |                         |        |
| S      | Static           |                         |        |
| D      | EIGRP            |                         |        |

<br>
<br>

What makes __EIGRP__ a __Distance Vector Protocol__?
~~~
!@CUCM
show ip protocols
show ip eigrp topology
~~~

<br>
<br>

### EIGRP Metric
*EIGRP Metric Formula*

<br>

1. Reported Distance (__RD__)  
2. Feasible Distance (__FD__)  
3. Successor (Primary : Lowest Cost)  
4. Feasible Successor (Backup)  

<br>

__Feasability Condition__ - An EIGRP route is a feasible successor route if the RD from the neighbor is less than the FD of the successor route.

<br>
<br>

---
&nbsp;

## 🔀 OSPF
*What device do you need to filter data entering your network? Firewall*

<br>

Which is the best firewall?
1. Palo Alto
2. Fortinet
3. Juniper
4. Cisco Firepower

<br>

What Routing protocol to use if __Multi-Vendor__? __OSPF__

&nbsp;
---
&nbsp;

### Single Area OSPF
~~~
!@CoreBABA
conf t
 router ospf 1
  router-id 10.#$34T#.#$34T#.4
  network 10.#$34T#.1.0 0.0.0.255 area 0
  network 10.#$34T#.#$34T#.0 0.0.0.255 area 0
  end
~~~

<br>

~~~
!@EDGE
conf t
 router ospf 1
  router-id #$34T#.0.0.1
  network 10.#$34T#.#$34T#.0 0.0.0.255 area 0
  network 200.0.0.0 0.0.0.255 area 0
  network #$34T#.0.0.1 0.0.0.0 area 0
  end
~~~

&nbsp;
---
&nbsp;

### OSPF Database
1. __`show ip ospf neighbors`__ : Neighbor Table
2. __`show ip ospf interface brief`__ : Interface Table
3. __`show ip ospf topology-info`__ : Topology Table

&nbsp;
---
&nbsp;

## Job Interview Question.
### What are the contents of an OSPF Hello Packet?

<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

<details>
<summary>Show Answer</summary>
	
- Router ID/Source OSPF Router
- Area ID
- Subnet Mask
- Authentication Type

- Hello Timer: 10
- Dead Timer: 40
- Designated Router
- Backup Designated Router

</details>

&nbsp;
---
&nbsp;

### Link-State Routing Protocol & Multi-Area OSPF
__LSU__ - Link-State Updates  
__LSA__ - Link-State Advertisement  

<br>

- Type 1 LSA - (__O__) Router LSA : Router info & Advertisements
- Type 2 LSA - (__O__) Network LSA : via DR/BDR Network Routes
- Type 3 LSA - (__O IA__) Summary LSA
- Type 5 LSA - (__O E2__) AS-External LSA

<br>

Summary LSA
~~~
!@EDGE
conf t
 int loopback 110
  ip add 10.#$34T#.110.110 255.255.255.255
  ip ospf 1 area #$34T#
  end
clear ip ospf process
yes
~~~

&nbsp;
---
&nbsp;

### OSPF States
D: __Down__ - The initial state where no hello packets have been received from a neighbor  
I: __Init__ - A hello packet has been received from a neighbor, but that neighbor's Router ID was not included in the hello packet, indicating a lack of bidirectional communication  
T: __Two-way__ - Bidirectional communication is established, as both routers have received each other's Router IDs in hello packets. DR/BDR Election occurs.  
E: __Exstart__ - Routers determine who will be the master and who will be the slave for the upcoming database exchange. The router with the higher Router ID becomes the master and begins the exchange of Database Description (DBD) packets, synchronizing sequence numbers.  
E: __Exchange__ - Routers exchange DBD packets to describe their Link State Databases (LSDBs). They compare the contents and identify any missing link-state information  
L: __Loading__ - Routers request the missing link-state information by sending Link-State Requests (LSRs). They then receive Link-State Updates (LSUs) and acknowledge them with Link-State Acknowledgements (LSAs)  
F: __Full__ - the LSDBs are fully synchronized and identical between the adjacent routers. The routers have all the necessary information to form a complete network map and are ready to share routing data  

<br>

Attempt to view OSPF States

~~~
!@R2 & R1
clear ip ospf process
yes
show ip ospf neighbor
~~~

<br>
<br>

---
&nbsp;

## Route Redistribution
~~~
!@CoreBABA
conf t
 router eigrp 100
  redistribute ospf 1 metric 10000 100 255 1 1500
  exit
 router ospf 1
  redistribute eigrp 100 subnets
end
~~~

&nbsp;
---
&nbsp;

## Path Selection Process : Admin Distance & Metric Cost
1. __Longest Prefix Match (LPM)__  
2. __Administrative Distance__
3. __Metric Cost__

<br>

| Legend | Routing Protocol | Administrative Distance | Metric |
| ---    | ---              | ---                     | ---    |
| C      | Connected        |                         |        |
| S      | Static           |                         |        |
| D      | EIGRP            |                         |        |
| D EX   | External EIGRP   |                         |        |
| O, OIA | OSPF             |                         |        |
| O E2   | External T5 OSPF |                         |        |

<br>
<br>

---
&nbsp;

## Tunneling and IP Security
*INET vs Private Line*

~~~
!@EDGE
conf t
 int gi 0/0/0
  no shut
  ip add 10.#$34T#.#$34T#.1 255.255.255.0
  ip nat inside
  desc INSIDE
 int gi 0/0/1
  no shut
  ip add 200.0.0.#$34T# 255.255.255.0
  ip nat outside
  desc OUTSIDE
 int loopback 0
  ip add #$34T#.0.0.1 255.255.255.255
  desc VIRTUALIP
 !
 ip access-list extended NAT-POLICY
  deny ip 10.#$34T#.0.0 0.0.255.255 10.11.0.0 0.0.255.255
  deny ip 10.#$34T#.0.0 0.0.255.255 10.12.0.0 0.0.255.255
  deny ip 10.#$34T#.0.0 0.0.255.255 10.21.0.0 0.0.255.255
  deny ip 10.#$34T#.0.0 0.0.255.255 10.22.0.0 0.0.255.255
  deny ip 10.#$34T#.0.0 0.0.255.255 10.31.0.0 0.0.255.255
  deny ip 10.#$34T#.0.0 0.0.255.255 10.32.0.0 0.0.255.255
  deny ip 10.#$34T#.0.0 0.0.255.255 10.41.0.0 0.0.255.255
  deny ip 10.#$34T#.0.0 0.0.255.255 10.42.0.0 0.0.255.255
  deny ip 10.#$34T#.0.0 0.0.255.255 10.51.0.0 0.0.255.255
  deny ip 10.#$34T#.0.0 0.0.255.255 10.52.0.0 0.0.255.255
  deny ip 10.#$34T#.0.0 0.0.255.255 10.61.0.0 0.0.255.255
  deny ip 10.#$34T#.0.0 0.0.255.255 10.62.0.0 0.0.255.255
  deny ip 10.#$34T#.0.0 0.0.255.255 10.71.0.0 0.0.255.255
  deny ip 10.#$34T#.0.0 0.0.255.255 10.72.0.0 0.0.255.255
  deny ip 10.#$34T#.0.0 0.0.255.255 10.81.0.0 0.0.255.255
  deny ip 10.#$34T#.0.0 0.0.255.255 10.82.0.0 0.0.255.255
  deny ip 10.#$34T#.0.0 0.0.255.255 10.91.0.0 0.0.255.255
  deny ip 10.#$34T#.0.0 0.0.255.255 10.92.0.0 0.0.255.255
  no deny ip 10.#$34T#.0.0 0.0.255.255 10.#$34T#.0.0 0.0.255.255
  permit ip any any
  exit
 !
 ip nat inside source list NAT-POLICY int g0/0/1 overload
 ip route 0.0.0.0 0.0.0.0 200.0.0.1
 !
 router ospf 1
  router-id #$34T#.0.0.1
  network 10.#$34T#.#$34T#.0 0.0.0.255 area 0
  !
  no network 200.0.0.0 0.0.0.255 area 0
  default-information originate always
  exit
  !
 ip name-server 8.8.8.8 8.8.4.4
 ip domain lookup
 ip domain lookup source int g0/0/0
 end
ping 8.8.8.8
ping google.com
~~~

<br>

### Tunneling (Unsecure)
~~~
!@EDGE
conf t
 int tun1
  ip add 172.16.1.#$34T# 255.255.255.0
  tunnel source g0/0/1
  tunnel mode gre multipoint
  no shut
  tun key 123
  ip nhrp authentication C1sc0123
  ip nhrp map multicast dynamic
  ip nhrp network-id 1337
  ip nhrp map 172.16.1.11 200.0.0.11
  ip nhrp map 172.16.1.12 200.0.0.12
  ip nhrp map 172.16.1.21 200.0.0.21
  ip nhrp map 172.16.1.22 200.0.0.22
  ip nhrp map 172.16.1.31 200.0.0.31
  ip nhrp map 172.16.1.32 200.0.0.32
  ip nhrp map 172.16.1.41 200.0.0.41
  ip nhrp map 172.16.1.42 200.0.0.42
  ip nhrp map 172.16.1.51 200.0.0.51
  ip nhrp map 172.16.1.52 200.0.0.52
  ip nhrp map 172.16.1.61 200.0.0.61
  ip nhrp map 172.16.1.62 200.0.0.62
  ip nhrp map 172.16.1.71 200.0.0.71
  ip nhrp map 172.16.1.72 200.0.0.72
  ip nhrp map 172.16.1.81 200.0.0.81
  ip nhrp map 172.16.1.82 200.0.0.82
  ip nhrp map 172.16.1.91 200.0.0.91
  ip nhrp map 172.16.1.92 200.0.0.92
  no ip nhrp map 172.16.1.#$34T# 200.0.0.#$34T#
  exit
 ip route 10.11.0.0 255.255.0.0 172.16.1.11 252
 ip route 10.12.0.0 255.255.0.0 172.16.1.12 252
 ip route 10.21.0.0 255.255.0.0 172.16.1.21 252
 ip route 10.22.0.0 255.255.0.0 172.16.1.22 252
 ip route 10.31.0.0 255.255.0.0 172.16.1.31 252
 ip route 10.32.0.0 255.255.0.0 172.16.1.32 252
 ip route 10.41.0.0 255.255.0.0 172.16.1.41 252
 ip route 10.42.0.0 255.255.0.0 172.16.1.42 252
 ip route 10.51.0.0 255.255.0.0 172.16.1.51 252
 ip route 10.52.0.0 255.255.0.0 172.16.1.52 252
 ip route 10.61.0.0 255.255.0.0 172.16.1.61 252
 ip route 10.62.0.0 255.255.0.0 172.16.1.62 252
 ip route 10.71.0.0 255.255.0.0 172.16.1.71 252
 ip route 10.72.0.0 255.255.0.0 172.16.1.72 252
 ip route 10.81.0.0 255.255.0.0 172.16.1.81 252
 ip route 10.82.0.0 255.255.0.0 172.16.1.82 252
 ip route 10.91.0.0 255.255.0.0 172.16.1.91 252
 ip route 10.92.0.0 255.255.0.0 172.16.1.92 252
 !
 no ip route 10.#$34T#.0.0 255.255.0.0 172.16.1.#$34T# 252
 end
~~~






6. ACL

7. NAT

8. IAM ACCESS MANAGEMENT Crypto Keys

9. RADIUS

10. STP


  
