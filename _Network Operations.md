
<!-- Your monitor number = #$34T# -->


## ⛅ Warm Up for Day 4.

<br>

### 🔧 Configure Day1 devices.

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
  ip add 10.#$34T#.72. 255.255.255.248
  no shut
  end
~~~

<br>

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



<br>

~~~



### Static Routing




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


  
