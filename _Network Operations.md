
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
 ip route 10.#$34T#.25.25 255.255.255.255 10.#$34T#.#$34T#.4
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

## 🔀 EIGRP
~~~
!@EDGE
conf t
 int loopback 100
  ip add 10.#$34T#.100.100 255.255.255.240
  desc EIGRP-NETWORK
  end
~~~





















Static Routing
Default Routing
EIGRP
OSPF
BGP

IGP
Link-State : OSPF (110) ISIS (115)

Distance Vector : RIP (120) , EIGRP (90)

EGP
BGP (WAN)


Configure

@EDGE OSPF AREA 0
OSPF AREA M

@CoreBABA 
OSPF AREA M
EIGRP 1

@CUCM
OSPF AREA M

EXBGP 20
INTBGP 200


---

6. ACL

7. NAT

8. IAM ACCESS MANAGEMENT Crypto Keys

9. RADIUS

10. STP


  
