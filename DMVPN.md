## DMVPN

### PRECONFIGS

~~~
!@UTM-PH
conf t
 hostname UTM-PH
 enable secret pass
 service password-encryption
 no logging cons
 ip domain lookup
 ip domain lookup source-interface G2
 ip name-server 192.168.102.8
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
 ip route 0.0.0.0 0.0.0.0 208.8.8.2
 end
wr
!
~~~


~~~
!@UTM-JP
conf t
 hostname UTM-JP
 enable secret pass
 service password-encryption
 no logging cons
 ip domain lookup
 ip domain lookup source-interface G2
 ip name-server 192.168.102.8
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
  no shut
 !
 username admin privilege 15 secret pass
 ip http server
 ip http secure-server
 ip http authentication local
 ip route 0.0.0.0 0.0.0.0 208.8.8.2
 end
wr
!
~~~


~~~
!@UTM-US
conf t
 hostname UTM-US
 enable secret pass
 service password-encryption
 no logging cons
 ip domain lookup
 ip domain lookup source-interface G2
 ip name-server 192.168.102.8
 line vty 0 14
  transport input all
  password pass
  login local
  exec-timeout 0 0
 int g1
  ip add 208.8.8.13 255.255.255.0
  no shut
 int g2
  ip add 192.168.102.13 255.255.255.0
  no shut
 int g3
  ip add 10.0.0.2 255.255.255.252
  no shut
 !
 username admin privilege 15 secret pass
 ip http server
 ip http secure-server
 ip http authentication local
 ip route 0.0.0.0 0.0.0.0 208.8.8.2
 end
wr
!
~~~


~~~
!@BLDG-PH
sudo su
ifconfig eth0 10.11.11.101 netmask 255.255.255.224 up
route add default gw 10.11.11.113
ping 10.11.11.113
~~~


~~~
!@BLDG-JP
sudo su
ifconfig eth0 10.21.21.211 netmask 255.255.255.240 up
route add default gw 10.21.21.213
ping 10.21.21.213
~~~


~~~
!@BLDG-US
sudo su
ifconfig eth0 10.0.0.1 netmask 255.255.255.252 up
route add default gw 10.0.0.2
ping 10.0.0.2
~~~








### STEP 1 - IKEV2

HUB
~~~
!@UTM-US
conf t
 crypto ikev2 proposal PROP1
  encryption _______
  integrity  _______
  group      _______
 !
 crypto ikev2 policy POL1
  proposal PROP1
 !
 crypto ikev2 keyring KEY1
  peer SPOKES
   address 0.0.0.0 0.0.0.0
   pre-shared-key keykeymo
 !
 crypto ikev2 profile IKEV2-PROF1
  match identity remote any
  authentication remote pre-share
  authentication local pre-share
  keyring local KEY1
  end
~~~


SPOKE
~~~
!@UTM-PH,UTM-JP
conf t
 crypto ikev2 proposal PROP1
  encryption _______
  integrity  _______
  group      _______
 !
 crypto ikev2 policy POL1
  proposal PROP1
 !
 crypto ikev2 keyring KEY1
  peer HUB
   address 208.8.8.13
   pre-shared-key keykeymo
 !
 crypto ikev2 profile IKEV2-PROF1
  match identity remote address 208.8.8.13
  authentication remote pre-share
  authentication local pre-share
  keyring local KEY1
  end
~~~



### STEP 2 - IPSEC

HUB
~~~
!@UTM-US
conf t
 crypto ipsec transform-set TS1  _______  _______
  mode tunnel
 !
 crypto ipsec profile IPSEC1
  set transform-set TS1
  set ikev2-profile  IKEV2-PROF1
 !
 interface Tunnel1
  ip address 172.16.0.100 255.255.255.0
  no shutdown
  tunnel source GigabitEthernet1
  tunnel mode gre multipoint
  tunnel protection ipsec profile IPSEC1
  !
  ip nhrp network-id 100
  ip nhrp map multicast dynamic
  ip nhrp authentication dmvpn
  ip nhrp redirect
  end
~~~


SPOKE
~~~
!@UTM-PH
conf t
 crypto ipsec transform-set TS1  _______  _______
  mode tunnel
 !
 crypto ipsec profile IPSEC1
  set transform-set TS1
  set ikev2-profile  IKEV2-PROF1
 !
 interface Tunnel1
  ip address 172.16.0.1 255.255.255.0
  no shutdown
  tunnel source GigabitEthernet1
  tunnel mode gre multipoint
  tunnel protection ipsec profile IPSEC1
  !
  ip nhrp network-id 100
  ip nhrp authentication dmvpn
  ip nhrp map 172.16.0.100 208.8.8.13
  ip nhrp map multicast 208.8.8.13
  ip nhrp nhs 172.16.0.100
  ip nhrp shortcut
  end
~~~


~~~
!@UTM-JP
conf t
 crypto ipsec transform-set TS1  _______  _______
  mode tunnel
 !
 crypto ipsec profile IPSEC1
  set transform-set TS1
  set ikev2-profile  IKEV2-PROF1
 !
 interface Tunnel1
  ip address 172.16.0.2 255.255.255.0
  no shutdown
  tunnel source GigabitEthernet1
  tunnel mode gre multipoint
  tunnel protection ipsec profile IPSEC1
  !
  ip nhrp network-id 100
  ip nhrp authentication dmvpn
  ip nhrp map 172.16.0.100 208.8.8.13
  ip nhrp map multicast 208.8.8.13
  ip nhrp nhs 172.16.0.100
  ip nhrp shortcut
  end
~~~



### STEP 3 - ROUTING

HUB
~~~
!@UTM-US
conf t
 router eigrp 100
  no auto-summary
  network 172.16.0.0 0.0.0.255
  network 10.0.0.0 0.0.0.3
  exit
 !
 interface Tunnel1
  no ip split-horizon eigrp 100
  no ip next-hop-self eigrp 100
  end
~~~


SPOKE
~~~
!@UTM-PH
conf t
 no router eigrp 100
 router eigrp 100
  no auto-summary
  network 172.16.0.0 0.0.0.255
  network 10.11.11.96 0.0.0.31
  end
~~~

~~~
!@UTM-JP
conf t
 no router eigrp 100
 router eigrp 100
  no auto-summary
  network 172.16.0.0 0.0.0.255
  network 10.21.21.208 0.0.0.15
  end
~~~




## DIGITAL SIGNATURE

### STEP 1 - Setup WinServer

| NetAdapter  | VMNet  | IP Address    | 
| ---         | ---    | ---           |
| 1           | NAT    | 208.8.8.8     |
| 2           | VMNet2 | 192.168.102.8 |

<br>

~~~
!@Powershell
set-netfirewallprofile -name private,public,domain -enabled false
rename-computer ccnp#$34T#.com
ncpa.cpl
~~~


&nbsp;
---
&nbsp;


### STEP 2 - Install Active Directory Domains and Services
Create a Service Account:
- Active Directory and Users and Computers

| New User    |              |
| ---         | ---          |
| User Name   | ca           |
| Full Name   | CERTAUTH     |
| Password    | C1sc0123     |
| Pass Policy | Never Expire |
| Member of   | IIS_IUSRS    |


&nbsp;
---
&nbsp;


### STEP 3 - Install Active Directory Certificate Services

Afterwards, install ADCS Add-Ons:
- Certificate Enrollment Policy Web Service  
- Certificate Enrollment Web Service         
- Certificate Authority Web Enrollment
- Network Device Enrollment Service


&nbsp;
---
&nbsp;


### STEP 4 - Create DNS Mapping for both Device
- Reverse Lookup Zone : 208.8.8.0
- A Record : utmph.ccnp#$34T#.com : 208.8.8.11
- A Record : utmjp.ccnp#$34T#.com : 208.8.8.12
- A Record : utmus.ccnp#$34T#.com : 208.8.8.13


&nbsp;
---
&nbsp;


### STEP 5 - Configure Certificates on Cisco UTM-PH & UTM-JP
~~~
!@UTM-US
conf t
 crypto key generate rsa modulus 2048 label CERTKEY
 !
 crypto pki trustpoint CCNPTRUST
  enrollment url http://192.168.102.8/certsrv/mscep/mscep.dll
  serial-number
  fqdn utmus.ccnp#$34T#.com
  ip-address 208.8.8.13
  subject-name CN=UTM-US,OU=HQ,O=RIVANCORP,L=MANILA,ST=NCR,C=PH
  subject-alt-name utmus.ccnp#$34T#.com
  revocation-check none
  source interface GigabitEthernet2
  rsakeypair CERTKEY
  end
~~~

<br>

~~~
!@UTM-PH
conf t
 crypto key generate rsa modulus 2048 label CERTKEY
 !
 crypto pki trustpoint CCNPTRUST
  enrollment url http://192.168.102.8/certsrv/mscep/mscep.dll
  serial-number
  fqdn utmph.ccnp#$34T#.com
  ip-address 208.8.8.11
  subject-name CN=UTM-PH,OU=NOC,O=RIVANCORP,L=MAKATI,ST=NCR,C=PH
  subject-alt-name utmph.ccnp#$34T#.com
  revocation-check none
  source interface GigabitEthernet2
  rsakeypair CERTKEY
  end
~~~

<br>

~~~
!@UTM-JP
conf t
 crypto key generate rsa modulus 2048 label CERTKEY
 !
 crypto pki trustpoint CCNPTRUST
  enrollment url http://192.168.102.8/certsrv/mscep/mscep.dll
  serial-number
  fqdn utmjp.ccnp#$34T#.com
  ip-address 208.8.8.12
  subject-name CN=UTM-JP,OU=NOC,O=RIVANCORP,L=TOKYO,ST=KANTO,C=JP
  subject-alt-name utmjp.ccnp#$34T#.com
  revocation-check none
  source interface GigabitEthernet2
  rsakeypair CERTKEY
  end
~~~


&nbsp;
---
&nbsp;


### STEP 6 - Access CA Web Enrollment

Set Routes for trustpoints:
~~~
!@cmd
route add 208.8.8.11 mask 255.255.255.255 192.168.102.11
route add 208.8.8.12 mask 255.255.255.255 192.168.102.12
route add 208.8.8.13 mask 255.255.255.255 192.168.102.13
~~~


<br>
<br>


http://192.168.102.8/certsrv/mscep/mscep.dll  

<br>
<br>

Grab the Hash & Challenge Password    
- Hash: ___________    
- Pass: ___________  


&nbsp;
---
&nbsp;


### STEP 7 - Enroll Network Devices

~~~
!@UTM-PH,UTM-JP
conf t
 crypto pki enroll CCNPTRUST
~~~


<br>
<br>

---
&nbsp;





### VERIFICATION - Modify DMVPN Tunnel to use RSA-SIGNATURE

~~~
!@UTM-US
conf t
 crypto ikev2 profile DMVPN-IKEV2
  match identity remote any
  no authentication remote pre-share
  authentication remote rsa-sig
  authentication local rsa-sig
  pki trustpoint CCNPTRUST
  end
~~~

~~~
!@UTM-PH,UTM-JP
conf t
 crypto ikev2 profile DMVPN-IKEV2
  match identity remote address 208.8.8.13
  no authentication remote pre-share
  authentication remote rsa-sig
  authentication local rsa-sig
  pki trustpoint CCNPTRUST
  end
~~~


<br>
<br>

---
&nbsp;


# DMVPN  :  FULL CONFIG

### PHASE1

~~~
!@UTM-US
conf t
 crypto ikev2 proposal PROPOSAL1
  encryption aes-cbc-256
  integrity sha256
  group 14
 !
 crypto ikev2 proposal PROPOSAL2
  encryption aes-gcm-256
  prf sha256
  group 14
 !
 crypto ikev2 policy POLICY1
  proposal PROPOSAL1
  proposal PROPOSAL2
 !
 crypto ikev2 keyring KEY1
  peer UTM-PH
   address 208.8.8.11 255.255.255.255
   pre-shared-key keykeymo
  peer UTM-JP
   address 208.8.8.12 255.255.255.255
   pre-shared-key keykeymo
 !
 crypto ikev2 profile PROF1
  match identity remote address 208.8.8.11 255.255.255.255
  match identity remote address 208.8.8.12 255.255.255.255
  authentication remote pre-share
  authentication local pre-share
  keyring local KEY1
 !
 end
~~~



~~~
!@UTM-PH
conf t
 crypto ikev2 proposal PROPOSAL1
  encryption aes-cbc-256
  integrity sha256
  group 14
 !
 crypto ikev2 proposal PROPOSAL2
  encryption aes-gcm-256
  prf sha256
  group 14
 !
 crypto ikev2 policy POLICY1
  proposal PROPOSAL1
  proposal PROPOSAL2
 !
 crypto ikev2 keyring KEY1
  peer UTM-US
   address 208.8.8.13 255.255.255.255
   pre-shared-key keykeymo
  peer UTM-JP
   address 208.8.8.12 255.255.255.255
   pre-shared-key keykeymo
 !
 crypto ikev2 profile PROF1
  match identity remote address 208.8.8.13 255.255.255.255
  match identity remote address 208.8.8.12 255.255.255.255
  authentication remote pre-share
  authentication local pre-share
  keyring local KEY1
 !
 end
~~~



~~~
!@UTM-JP
conf t
 crypto ikev2 proposal PROPOSAL1
  encryption aes-cbc-256
  integrity sha256
  group 14
 !
 crypto ikev2 proposal PROPOSAL2
  encryption aes-gcm-256
  prf sha256
  group 14
 !
 crypto ikev2 policy POLICY1
  proposal PROPOSAL1
  proposal PROPOSAL2
 !
 crypto ikev2 keyring KEY1
  peer UTM-US
   address 208.8.8.13 255.255.255.255
   pre-shared-key keykeymo
  peer UTM-JP
   address 208.8.8.11 255.255.255.255
   pre-shared-key keykeymo
 !
 crypto ikev2 profile PROF1
  match identity remote address 208.8.8.13 255.255.255.255
  match identity remote address 208.8.8.11 255.255.255.255
  authentication remote pre-share
  authentication local pre-share
  keyring local KEY1
 !
 end
~~~
 
 
 


### PHASE 2
~~~
!@UTM-US
conf t
 crypto ipsec transform-set TS1 esp-256-aes esp-sha256-hmac 
  mode tunnel
 crypto ipsec transform-set TS2 esp-256-aes esp-sha256-hmac 
  mode tunnel
  exit
 crypto ipsec profile IPSEC1
  set transform-set TS1 TS2
  set ikev2-profile PROF1
  exit
 int tun0
  ip add 172.16.1.13 255.255.255.0
  tunnel source g1
  tunnel mode gre multipoint
  tunnel protection ipsec profile IPSEC1
  !
  !
  ip nhrp network-id 100
  ip nhrp map multicast dynamic
  ip nhrp authentication keykeymo
  ip nhrp redirect
  end
~~~



~~~
!@UTM-PH
conf t
 crypto ipsec transform-set TS1 esp-256-aes esp-sha256-hmac 
  mode tunnel
 crypto ipsec transform-set TS2 esp-256-aes esp-sha256-hmac 
  mode tunnel
  exit
 crypto ipsec profile IPSEC1
  set transform-set TS1 TS2
  set ikev2-profile PROF1
  exit
 int tun0
  ip add 172.16.1.11 255.255.255.0
  tunnel source g1
  tunnel mode gre multipoint
  tunnel protection ipsec profile IPSEC1
  !
  !
  ip nhrp network-id 100
  ip nhrp nhs 172.16.1.13
  ip nhrp map 172.16.1.13 208.8.8.13
  ip nhrp map multicast 208.8.8.13
  ip nhrp authentication keykeymo
  ip nhrp shortcut
  end
~~~



~~~
!@UTM-JP
conf t
 crypto ipsec transform-set TS1 esp-256-aes esp-sha256-hmac 
  mode tunnel
 crypto ipsec transform-set TS2 esp-256-aes esp-sha256-hmac 
  mode tunnel
  exit
 crypto ipsec profile IPSEC1
  set transform-set TS1 TS2
  set ikev2-profile PROF1
  exit
 int tun0
  ip add 172.16.1.12 255.255.255.0
  tunnel source g1
  tunnel mode gre multipoint
  tunnel protection ipsec profile IPSEC1
  !
  !
  ip nhrp network-id 100
  ip nhrp nhs 172.16.1.13
  ip nhrp map 172.16.1.13 208.8.8.13
  ip nhrp map multicast 208.8.8.13
  ip nhrp authentication keykeymo
  ip nhrp shortcut
  end
~~~




## EIGRP
~~~
!@UTM-HQ
conf t
 router eigrp 100
  no auto-summary
  network 3.3.3.3 0.0.0.0
  network 172.16.1.0 0.0.0.255
  network 10.0.0.0 0.0.0.3
 int tun0
  no ip split-horizon eigrp 100
  no ip next-hop-self eigrp 100
  end
~~~


~~~
!@UTM-PH
conf t
 router eigrp 100
  no auto-summary
  network 1.1.1.1 0.0.0.0
  network 172.16.1.0 0.0.0.255
  network 10.11.11.96 0.0.0.31
 int tun0
  no ip split-horizon eigrp 100
  no ip next-hop-self eigrp 100
  end
~~~



~~~  
!@UTM-JP
conf t
 router eigrp 100
  no auto-summary
  network 2.2.2.2 0.0.0.0
  network 172.16.1.0 0.0.0.255
  network 10.21.21.208 0.0.0.15
 int tun0
  no ip split-horizon eigrp 100
  no ip next-hop-self eigrp 100
  end
~~~



## OSPF

~~~
!@UTM-US
conf t
 router ospf 1
  network 3.3.3.3 0.0.0.0 area 0
  network 172.16.1.0 0.0.0.255 area 0
  network 10.0.0.0 0.0.0.3 area 0
 int tun0
  ip ospf network point-to-multipoint
  ip mtu 1400
  ip tcp adjust-mss 1360
  bandwidth 1000000
  delay 1000
  end
~~~



~~~
!@UTM-PH
conf t
 router ospf 1
  network 1.1.1.1 0.0.0.0 area 0
  network 172.16.1.0 0.0.0.255 area 0
  network 10.11.11.96 0.0.0.31 area 0
 int tun0
  ip ospf network point-to-multipoint
  ip mtu 1400
  ip tcp adjust-mss 1360
  bandwidth 1000000
  delay 1000
  end
~~~



~~~
!@UTM-JP
conf t
 router ospf 1
  network 2.2.2.2 0.0.0.0 area 0
  network 172.16.1.0 0.0.0.255 area 0
  network 10.21.21.208 0.0.0.15 area 0
 int tun0
  ip ospf network point-to-multipoint
  ip mtu 1400
  ip tcp adjust-mss 1360
  bandwidth 1000000
  delay 1000
  end
~~~




## OSPF

~~~
!@UTM-US
conf t
 router ospf 1
  network 3.3.3.3 0.0.0.0 area 0
  network 172.16.1.0 0.0.0.255 area 0
  network 10.0.0.0 0.0.0.3 area 0
 int tun0
  ip ospf network point-to-multipoint
  ip mtu 1400
  ip tcp adjust-mss 1360
  bandwidth 1000000
  delay 1000
  end
~~~



~~~
!@UTM-PH
conf t
 router ospf 1
  network 1.1.1.1 0.0.0.0 area 0
  network 172.16.1.0 0.0.0.255 area 0
  network 10.11.11.96 0.0.0.31 area 0
 int tun0
  ip ospf network point-to-multipoint
  ip mtu 1400
  ip tcp adjust-mss 1360
  bandwidth 1000000
  delay 1000
  end
~~~



~~~  
!@UTM-JP
conf t
 router ospf 1
  network 2.2.2.2 0.0.0.0 area 0
  network 172.16.1.0 0.0.0.255 area 0
  network 10.21.21.208 0.0.0.15 area 0
 int tun0
  ip ospf network point-to-multipoint
  ip mtu 1400
  ip tcp adjust-mss 1360
  bandwidth 1000000
  delay 1000
  end
~~~
