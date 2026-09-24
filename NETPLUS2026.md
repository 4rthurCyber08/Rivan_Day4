
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


## RSTHayup Setup

### VLAN Assignment

~~~
!@A1
conf t
 int e0/0
  switchport mode access
  switchport access vlan 10
  end
~~~

~~~
!@A2
conf t
 int e1/0
  switchport mode access
  switchport access vlan 10
  end
~~~


&nbsp;
---
&nbsp;


### IP Assignment

~~~
!@P1
conf t
 int e0/0
  no shut
  ip add 10.2.1.101 255.255.255.0
  end
show ip int brief | ex una
~~~


~~~
!@P2
conf t
 int e1/0
  no shut
  ip add 10.2.1.102 255.255.255.0
  end
show ip int brief | ex una
~~~


&nbsp;
---
&nbsp;


### EIGRP

~~~
!@R4
conf t
 router eigrp 100
  no auto-summary
  network 10.1.4.8 0.0.0.3
  network 10.1.4.4 0.0.0.3
  end
~~~


~~~
!@C1
config t
 router eigrp 100
  no auto-summary
  network 10.1.4.4 0.0.0.3
  network 10.2.1.0 0.0.0.255
  network 10.2.2.0 0.0.0.255
  network 192.168.1.128 0.0.0.31
end
~~~


~~~
!@C2
conf t
 router eigrp 100
  no auto-summary
  network 10.1.4.8 0.0.0.3
  network 10.2.1.0 0.0.0.255
  network 10.2.2.0 0.0.0.255
  network 192.168.1.128 0.0.0.31
  end
~~~


&nbsp;
---
&nbsp;


### OSPF
*What device do you need to filter data entering your network? Firewall*

<br>

Which is the best firewall?
1. Palo Alto
2. Fortinet
3. Juniper
4. Cisco Firepower

<br>

What Routing protocol to use if __Multi-Vendor__? __OSPF__

<br>
<br>

### Single Area OSPF

~~~
!@R3
conf t
 router ospf 1
  router-id 3.3.3.3
  network 3.3.3.3 0.0.0.0 area 0
  network 10.1.1.8 0.0.0.3 area 0
  network 10.1.1.4 0.0.0.3 area 0
  end
~~~


~~~
!@R4
conf t
 router ___  __
  router-id __.__.__.__
  network __.__.__.__  __.__.__.__ area __
  network __.__.__.__  __.__.__.__ area __
  end
~~~


~~~
!@R2
conf t
 router ospf 1
  router-id 2.2.2.2
  network 2.2.2.2 0.0.0.0 area 0
  network 10.1.1.0 0.0.0.3 area 0
  network 10.1.1.4 0.0.0.3 area 0
  end
~~~


~~~
!@R1
conf t
 router ospf 1
  router-id 2.2.2.2
  network 2.2.2.2 0.0.0.0 area 0
  network 10.1.1.0 0.0.0.3 area 0
  network 10.1.1.4 0.0.0.3 area 0
  end
~~~


&nbsp;
---
&nbsp;


### Redistribution
~~~
!@R4
config T
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


## Path Selection Rules
1. Longest Prefix Match
2. Lowest Admin Distance
3. Lowest Metric/Cost



### Ex. Which path is chosen to reach a host with the IP of 10.25.60.148

D     10.25.60.0/24   
D EX  10.25.60.192/26
R     10.25.60.128/25
O     10.25.56.0/21  
O IA  10.25.58.0/23  


&nbsp;
---
&nbsp;


### Ex. Which path is chosen to reach a host with the IP of 10.25.60.148

D     10.25.60.0/24   
O     10.25.60.0/24   
L2    10.25.60.0/24   
B     10.25.60.0/24


&nbsp;
---
&nbsp;


### Ex. Which path is chosen to reach a host with the IP of 10.25.60.148

D     10.25.60.0/24   [90/356241]
D     10.25.60.192/26 [170/645521]
D     10.25.60.128/25 [120/69360420]
D     10.25.56.0/21   [110/2560]
D     10.25.58.0/23   [110/512602]


<br>
<br>

---
&nbsp;


### Firewall Setup

~~~
!@FW-VM
config system global
 set hostname FW-VM
 end
#
config system interface
 edit port1
  set vdom root
  set type physical
  set mode static
  set allowaccess  ping https ssh http fgfm telnet
  set ip 208.8.8.69/24
  set status up
  next
 edit loopback0
  set vdom root
  set type loopback
  set ip 69.69.69.69/32
  set allowaccess  ping https ssh http fgfm telnet
  set status up
  end
#
~~~


&nbsp;
---
&nbsp;


### Connect FW-VM  and  R1

~~~
!@R4
conf t
 int e3/3
  no shut
  ip add 10.10.10.1 255.255.255.252
 !
 router ospf 1
  network 10.10.10.0 0.0.0.3 area 0
  end
~~~


~~~
!@FW-VM
config system interface
 edit port2
  set vdom root
  set mode static
  set ip 10.10.10.2 255.255.255.252
   set allowaccess ping https ssh http telnet fgfm
  set status up
  end
~~~


&nbsp;
---
&nbsp;


### Configure OSPF for FW-VM
~~~
!@FW-VM
config router ospf 
 set router-id 69.69.69.69
 config area 
  edit 0.0.0.0
  end
 config network
  edit 1
   set prefix 69.69.69.69/32
   set area 0.0.0.0
   set comments LOOPBACK
   next
  edit 2
   set prefix 10.10.10.0/30
   set area 0.0.0.0
   set comments LAN
   end
  end
get router info ospf neigh
get router info routing-table all
~~~


&nbsp;
---
&nbsp;


### Provide INTERNET
~~~
!@FW-VM
config router static
 edit 1
  set dst 0.0.0.0/0
  set device port1
  set gateway 208.8.8.2
  end
get router info routing-table all
~~~


~~~
!@FW-VM
config router ospf 
 set default-information-originate enable
 end
~~~


&nbsp;
---
&nbsp;


### Configure Policy

~~~
!@FW-VM
config firewall policy
 edit 1
  set name INSIDE-TO-OUTSIDE
  set srcintf port2
  set dstintf port1
  set srcaddr all
  set dstaddr all
  set action accept 
  set schedule always
  set service ALL
  set nat enable
  next
 edit 2
  set name OUTSIDE-TO-INSIDE
  set srcintf port1
  set dstintf port2
  set srcaddr all
  set dstaddr all
  set action accept 
  set schedule always
  set service ALL
  set nat disable
  end
show firewall policy
~~~


&nbsp;
---
&nbsp;


### Verify Connectivity
~~~
!@R4
ping 8.8.8.8
~~~

~~~
!@FW-VM
get system session list | grep 'icmp\|PROTO'
~~~


<br>
<br>

---
&nbsp;


## Packet Filtering
~~~
!@P1
conf t
 ip domain lookup
 ip name-server 8.8.8.8
 end
~~~





<br>


### Protect your Brain


### Create a standard ACL named FWP1 to protect your brain
~~~
!@R4
config t
 no ip access-list standard FWP1
 ip access-list standard FWP1
  deny __.__.__.__  __.__.__.__
  deny __.__.__.__  __.__.__.__
  deny __.__.__.__  __.__.__.__
  permit any
 int e3/3
  ip access-group FWP1 in
  end
show ip access-lists int e3/3
~~~



__Remove the Policy__
~~~
!@R4
conf t
 int e3/3
  no ip access-group FWP1 in
  end
~~~


&nbsp;
---
&nbsp;


### Create an extended ACL named FWP2
~~~
!@P1
www.thepiratebay.org
www.limetorrents.com
www.torlock2.com
www.kickasstorrents.com
~~~

~~~
!@R4
config t
 no ip access-list standard FWP2
 ip access-list standard FWP2
  deny __.__.__.__  __.__.__.__
  deny __.__.__.__  __.__.__.__
  deny __.__.__.__  __.__.__.__
  permit any
 int e3/3
  ip access-group FWP2 in
  end
show ip access-lists int e3/3
~~~


&nbsp;
---
&nbsp;


### Create an extended ACL named FWP3
Enable Services
~~~
!@Powrshell
Add-WindowsCapability -Online -Name OpenSSH.Server
start-service sshd
~~~


Prevent the ff:
- P1 from accessing SMB     on 208.8.8.1


Recipe:
  [ACTION]  [PROTOCOL]  [SOURCE]  [DESTINATION]  [PORT]


~~~
!@R4
config t
 no ip access-list extended FWP3
 ip access-list extended FWP3
  deny tcp host 10.2.1.101  208.8.8.1 0.0.0.0  eq 445
  permit ip any any
 int e3/3
  ip access-group FWP3 out
  end
show ip access-lists int e3/3
~~~


&nbsp;
---
&nbsp;


### Create an extended ACL named FWP4
Prevent the ff:
- P1 from accessing SSH   on 208.8.8.1
- P2 from accessing DNS
- P2 from Pinging 

~~~
!@R4
config t
 no ip access-list extended FWP4
 ip access-list extended FWP4
   ???
   ???
 int e3/3
  ip access-group FWP4 out
  end
show ip access-lists int e3/3
~~~



&nbsp;
---
&nbsp;


### Stateless vs Statefull
~~~
!@cmd
route add 10.2.1.101  mask 255.255.255.255  208.8.8.69
~~~


<br>


~~~
!@P1
telnet 208.8.8.1 445
~~~


<br>


__Capture TCP Packets__
~~~
!@Wireshark
!tcp.analysis.out_of_order && tcp && !tcp.analysis.duplicate_ack
~~~


<br>


__Telnet RST P1 from PC__
~~~
!@cmd
ssh -o KexAlgorithms=+diffie-hellman-group14-sha1 -o HostKeyAlgorithms=+ssh-rsa -l admin 10.2.1.101
~~~


<br>
<br>

---
&nbsp;


## NAT/PAT

~~~
!@FW-VM
get system session list | grep 'icmp\|PROTO'
~~~


<br>
<br>

---
&nbsp;


## Reverse Proxy
~~~
!@P1
conf t
 username admin priv 15 secret pass
 ip domain name key.sec
 crypto key generate rsa modulus 2048
 ip ssh version 2
 line vty 0 4
  transport input all
  login local
  exit
 service finger
 service tcp-small-servers
 service udp-small-servers
 ip dns server
 ip http server
 ip http secure-server
 telephony-service
  no auto-reg-ephone
  max-ephones 5
  max-dn 20
  ip source-address 10.2.1.101 port 2000
  exit
 voice service voip
  allow-connections h323 to sip
          
  allow-connections sip to h323
  allow-connections sip to sip
  supplementary-service h450.12
 sip
   bind control source-interface e0/0
   bind media source-interface e0/0
   registrar server expires max 600 min 60
 voice register global
  mode cme
  source-address 10.2.1.101 port 5060
  max-dn 12
  max-pool 12
  authenticate register
  create profile sync syncinfo.xml
  end
~~~


~~~
!@P2
conf t
 username admin priv 15 secret pass
 ip domain name key.sec
 crypto key generate rsa modulus 2048
 ip ssh version 2
 line vty 0 4
  transport input all
  login local
  exit
 service finger
 service tcp-small-servers
 service udp-small-servers
 ip dns server
 ip http server
 ip http secure-server
 telephony-service
  no auto-reg-ephone
  max-ephones 5
  max-dn 20
  ip source-address 10.2.1.102 port 2000
  exit
 voice service voip
  allow-connections h323 to sip
          
  allow-connections sip to h323
  allow-connections sip to sip
  supplementary-service h450.12
 sip
   bind control source-interface e1/0
   bind media source-interface e1/0
   registrar server expires max 600 min 60
 voice register global
  mode cme
  source-address 10.2.1.102 port 5060
  max-dn 12
  max-pool 12
  authenticate register
  create profile sync syncinfo.xml
  end
~~~


<br>
<br>

---
&nbsp;


### Expose P1 to the internet via the ff
- 10.2.1.101  80  > 208.8.8.80  8080


<br>
<br>

---
&nbsp;


### Expose P2 to the internet via the ff
- 10.2.1.101  443  > 208.8.8.80  8443
- 10.2.1.101  22   > 208.8.8.80  2222


&nbsp;
---
&nbsp;


### Expose P2 to the internet via the ff
- 10.2.1.102  80   > 208.8.8.80  8081
- 10.2.1.102  23   > 208.8.8.80  1233
- 10.2.1.102  22   > 208.8.8.80  2022



<br>
<br>

---
&nbsp;


# Logging & Monitoring

### Setup

__IR-ElasticSys__
| NetAdapter | VMNet   |
| ---        | ---     |
| 1          | NAT     |
| 2          | VMNet 2 |


__CSR1000v / R1__
| NetAdapter | VMNet   |
| ---        | ---     |
| 1          | NAT     |
| 2          | VMNet 2 |
| 3          | VMNet 3 |


<br>
<br>

---
&nbsp;


## Set the correct Time (REAL WORLD USE NTP)
~~~
!@IR-ElasticSys
timedatectl set-timezone UTC
timedatectl set-timezone Asia/Kuala_Lumpur
date
~~~


~~~
!@R1
conf t
 int g1
  ip add 208.8.8.11 255.255.255.0 
  no shut
 ip route 0.0.0.0 0.0.0.0 208.8.8.2
 ip name-server 8.8.8.8   1.1.1.1
 !
 int g2
  ip add 192.168.102.11 255.255.255.0
  no shut
 int g3
  ip add 192.168.103.11 255.255.255.0
  no shut
 !
 ntp server 216.239.35.12
 clock timezone PHT 8
 end
show clock
show ntp associations
sh ntp status
show clock
~~~


&nbsp;
---
&nbsp;


### 1. Turn On ElasticSearch
- Elastic Search MUST be running
- Filebeat MUST be listening on port 2055 for netflow traffic


<br>
<br>


### 2. Access ElasticSearch GUI

http://208.8.8.133:5601
- Username: admin
- Password: C1sc0123


<br>
<br>

---
&nbsp;


### Network Monitoring: Syslogs

~~~
!@R4
conf t
 service timestamps log datetime msec
 service sequence-numbers
 !
 archive
  log config
   notify syslog
   exit
  exit
 ip nat log translations syslog bind-only 
 !
 logging host 208.8.8.133 transport udp port 9001
 logging source-interface e3/3
 logging on
end
~~~



<br>
<br>

---
&nbsp;


### Log Severity Levels

| Level | Severity      | Description                       |
| ---   | ---           | ---                               |
| 0     | Emergency     | System is unusable                |
| 1     | Alert         | Immediate action required         |
| 2     | Critical      | Critical conditions               | Shut gig3
| 3     | Error         | Error conditions                  | Disconnect LAN Card |
| 4     | Warning       | Warning conditions                |
| 5     | Notice        | Normal but significant conditions | Ping 11.11.11.11 |
| 6     | Informational | Informational messages            | 
| 7     | Debug         | Debugging messages                |


<br>

*log.level : "informational"  or log.level : "notification" or log.level : "warning" or log.level : "error" or log.level : "critical" or log.level : "alert" or log.level : "emergency"*

- Severity: how important the log is
- Facility: where the log came from

~~~
!@R4
conf t
 service timestamps log datetime msec
 service sequence-numbers
 logging host 208.8.8.133 transport udp port 9001
 logging source-interface g2
 logging on
 logging facility local7
 !
 logging trap 6   ! from 0 - 6
end
~~~

<br>

__Track Logins__
~~~
!@R4
conf t
 username admin priv 15 secret pass
 ip domain name SYSLOG.COM
 crypto key generate rsa modulus 2048 
 ip ssh version 2
 !
 line vty 0 4
  transport input all
  login local
  login on-success log
  login on-failure log
  end
~~~


<br>
<br>

---
&nbsp;


## SNMPv2, v3

### Setup

Devices:
- 1x CSR1000v
- 1x Zabbix

CSR1000v:
  Name: UTM-PH
  
  | NetAdapter   |        |
  | ---          | ---    |
  | NetAdapter   | NAT    |
  | NetAdapter 2 | VMNet2 |
  | NetAdapter 3 | VMNet3 |
  

Zabbix:
  Name: Zabbix_appliance-7.4.6
  
  | NetAdapter   |        |
  | ---          | ---    |
  | NetAdapter   | NAT    |
  
  

### Bootstrap
~~~
!@zabbix
Login: root
Pass:  zabbix

# ip -4 addr

Get IP Address and access via Web using the ff credentials:
Login: Admin
Pass:  zabbix
~~~


~~~
!@UTM-PH
conf t
 hostname UTM-PH
 enable secret pass
 service password-encryption
 no logging cons
 no ip domain lookup
 line vty 0 14
  transport input all
  password pass
  login local
  exec-timeout 0 0
 int g1
  ip add 208.8.8.11 255.255.255.0
  no shut
 int g2
  ip add 192.168.102.11 255.255.255.0
  no shut
 int g3
  ip add 192.168.103.11 255.255.255.0
  no shut
 !
 username admin privilege 15 secret pass
 ip http server
 ip http secure-server
 ip http authentication local
 end
wr
!
~~~


<br>
<br>

---
&nbsp;


### Setup Zabbix


### SNMPv2 
~~~
!@UTM-PH
conf t
 ip access-list extended SNMP
  permit ip host 208.8.8.132 any   !zabbix ip
  exit
 !
 snmp-server community C1sc0123 ro SNMP
 end
~~~


If SNMP is not available on Zabbix GUI
~~~
!@Zabbix
systemctl restart zabbix-server
~~~


<br>
<br>

---
&nbsp;


### SNMPv3

~~~
!@UTM-PH
conf t
 snmp-server group SUPERADMIN v3 priv
 snmp-server group NOC        v3 priv
 snmp-server group SOC        v3 priv
 !
 snmp-server user admin SUPERADMIN v3 auth sha C1sc0123 priv aes 256 C1sc0123 
 end
~~~


SNMP Access
~~~
!@UTM-PH
conf t
 ip access-list extended SNMPv3
  remark SNMPv3-SERVER-ZABBIX
  permit ip host 208.8.8.132 any
  exit
 !
 snmp-server view SNMP-V3-RO-VIEW iso included
 snmp-server view SNMP-V3-RW-VIEW iso included
 ! 
 snmp-server group SUPERADMIN v3 priv write SNMP-V3-RW-VIEW access SNMPv3
 snmp-server group NOC        v3 priv write SNMP-V3-RW-VIEW access SNMPv3
 snmp-server group SOC        v3 priv write SNMP-V3-RW-VIEW access SNMPv3
 !
 snmp-server user admin2 SNMP-V3-RW-VIEW v3 auth sha C1sc0123 priv aes 256 C1sc0123 
 end
~~~


<br>
<br>

---
&nbsp;


## AAA - RADIUS (Wired & Wireless)
> [!IMPORTANT]
> Configure WinServer 2022 for a RADIUS Server

<br>

Requirements:
- ACTIVE DIRECTORY
- NETWORK POLICY SERVER (RADIUS)

<br>

~~~
!@Cisco
conf t
 username admin privilege 15 secret pass
 aaa new-model
 radius server WINRAD
  address ipv4 10.#$34T#.1.8 auth-port 1812 acct-port 1813
  key keykeymo
  exit
 aaa group server radius RADGROUP
  server name WINRAD
  exit
 aaa authentication login default group RADGROUP local
 aaa authorization exec default group RADGROUP local
 line vty 0 14
  login authentication default
  end
~~~


<br>
<br>

---
&nbsp;


## Lab Setup

### 1. Deploy

Devices:
- 2x CSR1000v
- 1x NetOps
- 3x TinyCore (yvm.ova)

CSR1000v:
  Name: UTM-PH
  
  | NetAdapter   |        |
  | ---          | ---    |
  | NetAdapter   | NAT    |
  | NetAdapter 2 | VMNet2 |
  | NetAdapter 3 | VMNet3 |
  

CSR1000v:
  Name: UTM-JP
  
  | NetAdapter   |        |
  | ---          | ---    |
  | NetAdapter   | NAT    |
  | NetAdapter 2 | VMNet2 |
  | NetAdapter 3 | VMNet4 |

NetOps:
  Name: NetOps-PH
  
  | NetAdapter   |                    |
  | ---          | ---                |
  | NetAdapter   | VMNet1             |
  | NetAdapter 2 | VMNet2             |
  | NetAdapter 3 | VMNet3             |
  | NetAdapter 4 | Bridge (Replicate) |

TinyCore (yvm.ova):
  Name: BLDG-PH
  
  | NetAdapter   |                    |
  | ---          | ---                |
  | NetAdapter   | VMNet3             |
  
TinyCore (yvm.ova):
  Name: BLDG-JP-1
  
  | NetAdapter   |                    |
  | ---          | ---                |
  | NetAdapter   | VMNet4             |

TinyCore (yvm.ova):
  Name: BLDG-JP-2
  
  | NetAdapter   |                    |
  | ---          | ---                |
  | NetAdapter   | VMNet4             |


### 2. Bootstrap
~~~
!@UTM-PH
conf t
 hostname UTM-PH
 enable secret pass
 service password-encryption
 no logging cons
 no ip domain lookup
 line vty 0 14
  transport input all
  password pass
  login local
  exec-timeout 0 0
 int g1
  ip add 208.8.8.11 255.255.255.0
  no shut
 int g2
  ip add 192.168.102.11 255.255.255.0
  no shut
 int g3
  ip add 10.11.11.113 255.255.255.224
  no shut
 !
 username admin privilege 15 secret pass
 ip http server
 ip http secure-server
 ip http authentication local
 end
wr
!
~~~

<br>

~~~
!@UTM-JP
conf t
 hostname UTM-JP
 enable secret pass
 service password-encryption
 no logging cons
 no ip domain lookup
 line vty 0 14
  transport input all
  password pass
  login local 
  exec-timeout 0 0
 int g1
  ip add 208.8.8.12 255.255.255.0
  no shut
 int g2
  ip add 192.168.102.12 255.255.255.0
  no shut
 int g3
  ip add 10.21.21.213 255.255.255.240
  ip add 10.22.22.223 255.255.255.192 secondary
  no shut
 !
 username admin privilege 15 secret pass
 ip http server
 ip http secure-server
 ip http authentication local
 end
wr
!
~~~

<br>

~~~
!@BLDG-PH
sudo su
hostname BLDG-PH
ifconfig eth0 10.11.11.101 netmask 255.255.255.224 up
route add default gw 10.11.11.113
ping 10.11.11.113
~~~

<br>

~~~
!@BLDG-JP-1
sudo su
hostname BLDG-JP-1
ifconfig eth0 10.21.21.211 netmask 255.255.255.240 up
route add default gw 10.21.21.213
ping 10.21.21.213
~~~

<br>

~~~
!@BLDG-JP-2
sudo su
hostname BLDG-JP-2
ifconfig eth0 10.22.22.221 netmask 255.255.255.192 up
route add default gw 10.22.22.223
ping 10.22.22.223
~~~

<br>


### NetOps-PH Setup
> Login: root
> Pass: C1sc0123

1. Get the MAC Address for the Bridge connection
VMWare > NetOps-PH Settings > NetAdapter (2, 3, & 4) > Advance > MAC Address

| NetAdapter   | MAC Address      | VM Interface |
| NetAdapter 2 | ___.___.___.___  | ens___       |  ens192
| NetAdapter 3 | ___.___.___.___  | ens___       |  ens224
| NetAdapter 4 | ___.___.___.___  | ens___       |  ens256

<br>

2. Get Network-VM Mapping
~~~
!@NetOps-PH
ip -br link
~~~

<br>

3. Modify Interface IP
VMNet2:  192.168.102.6/24
VMNet3:  10.11.11.100/27
Bridged: 10.#$34T#.1.6/24

<br>

~~~
!@NetOps-PH
ifconfig ens192 192.168.102.6 netmask 255.255.255.0 up
ifconfig ens224 10.11.11.100 netmask 255.255.255.224 up
ifconfig ens256 10.#$34T#.1.6 netmask 255.255.255.0 up
~~~

<br>

Verify:
~~~
!@NetOps-PH
ip -4 addr

nmcli connection show
netstat -rn
~~~

<br>

or  

<br>

__Using Network Management CLI for persistent IP.__

<br>

~~~
!@NetOps-PH
nmcli connection add \
type ethernet \
con-name VMNET2 \
ifname ens192 \
ipv4.method manual \
ipv4.addresses 192.168.102.6/24 \
autoconnect yes

nmcli connection up VMNET2

nmcli connection add \
type ethernet \
con-name VMNET3 \
ifname ens224 \
ipv4.method manual \
ipv4.addresses 10.11.11.100/27 \
autoconnect yes

nmcli connection up VMNET3

nmcli connection add \
type ethernet \
con-name BRIDGED \
ifname ens256 \
ipv4.method manual \
ipv4.addresses 10.#$34T#.1.6/24 \
autoconnect yes

nmcli connection up BRIDGED

ip route add 10.0.0.0/8 via 10.#$34T#.1.4 dev ens256
ip route add 200.0.0.0/24 via 10.#$34T#.1.4 dev ens256
ip route add 0.0.0.0/0 via 10.11.11.113 dev ens224
~~~


### Remote Access
Connect to Management Interfaces of Devices

NetOps-PH: 192.168.102.6
UTM-PH: 192.168.102.11
UTM-JP: 192.168.102.12


<br>
<br>

---
&nbsp;

## Site-to-Site VPN & Cryptography

### 1. Create a Key Pair for both UTM Routers

~~~
!@UTM-PH & UTM-JP
conf t
 ip domain name sec.plus
 !
 crypto key generate rsa modulus 2048 label key exportable
 ip ssh version 2
 ip ssh rsa keypair-name key
 end
show ip ssh
~~~

<br>


View Private & Public Keys
~~~
!@UTM-PH & UTM-JP
conf t
 crypto key export rsa key pem terminal aes C1sc0123
 end
~~~

<br>

### Diffie-Hellman Key Exchange 
Ref: https://sec.cloudapps.cisco.com/security/center/resources/next_generation_cryptography

<br>

| DH GROUP | MODP                      | EC  |
| ---      | ---                       | --- |
| 1 	   | 768                       |     |
| 2 	   | 1024                      |     |
| 5 	   | 1536                      |     |
| 14 	   | 2048                      |     |
| 15 	   | 3072                      |     |
| 16 	   | 4096                      |     |
| 17 	   | 6144                      |     |
| 18 	   | 8192                      |     |
| 19       |                           | 256 |
| 20       |                           | 384 |
| 21       |                           | 521 |
| 24       | 2048 Prime order 256 bits |     |

<br>

~~~
!@NetOps-PH
mkdir crypto; cd crypto
openssl dhparam -out dhgroup.pem 1024
~~~

<br>

~~~
openssl genpkey -paramfile dhgroup.pem -out ph_priv.key
openssl genpkey -paramfile dhgroup.pem -out jp_priv.key
~~~

<br>

~~~
openssl pkey -in ph_priv.key -pubout -out ph_pub.key
openssl pkey -in jp_priv.key -pubout -out jp_pub.key
~~~

<br>

~~~
openssl pkeyutl -derive -inkey ph_priv.key -peerkey jp_pub.key -out ph-shared.secret
openssl pkeyutl -derive -inkey jp_priv.key -peerkey ph_pub.key -out jp-shared.secret
~~~

<br>

View Private key contents
~~~
!@NetOps
openssl pkey -in rsa_priv.key -text -noout
~~~

<br>

### 2. Access the GUI of Both UTM Routers

UTM-PH: https://192.168.102.11
UTM-JP: https://192.168.102.12

<br>

Wireshark: ssh vs telnet vs esp
