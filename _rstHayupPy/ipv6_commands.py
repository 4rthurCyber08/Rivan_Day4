# commands to be pushed to cli
i1_commands = [
    # --ipv6
    'ipv6 unicast-routing',
    
	'interface ethernet 1/2',
	'ipv6 add b:1:4:b::4/64',
    'exit',
    
	'interface ethernet 1/1',
	'ipv6 add b:2:1:b::4/64',
    'exit',
    
	'interface ethernet 1/3',
	'ipv6 add b:1:11:b::4/64',
	'exit',
 
    'interface loopback 1',
    'ipv6 add b44::1/128',
    'exit',
    
    'router bgp 45',
    'neigh b:1:4:b::5 remote-as 45',
    'neigh b:2:1:b::2 remote-as 2',
    'neigh b:1:11:b::1 remote-as 1',
    'address-family ipv6',
    'neigh b:1:4:b::5 activate',
    'neigh b:2:1:b::2 activate',
    'neigh b:1:11:b::1 activate',
    'network b:1:4:b::/64',
    'network b:2:1:b::/64',
    'network b:1:11:b::/64',
    'network b44::1/128',
    'exit',
    'exit'
]

i2_commands = [
    # --ipv6
    'ipv6 unicast-routing',
    
	'interface ethernet 0/2',
	'ipv6 add b:2:4:b::2/64',
	'exit',
 
	'interface ethernet 1/1',
	'ipv6 add b:2:1:b::2/64',
	'exit',
 
	'interface ethernet 1/3',
	'ipv6 add b:1:22:b::2/64',
	'exit',
 
	'interface ethernet 1/2',
	'ipv6 add b:1:2:b::2/64',
	'exit',
 
    'interface loopback 2',
    'ipv6 add b22::1/128',
    'exit',
    
    'router bgp 2',
    'neigh b:2:1:b::4 remote-as 45',
    'neigh b:2:4:b::5 remote-as 45',
    'neigh b:1:2:b::3 remote-as 3',
    'neigh b:1:22:b::1 remote-as 1',
    'address-family ipv6',
    'neigh b:2:4:b::5 activate',
    'neigh b:2:1:b::4 activate',
    'neigh b:1:2:b::3 activate',
    'neigh b:1:22:b::1 activate',
    'network b:2:4:b::/64',
    'network b:1:2:b::/64',
    'network b:2:1:b::/64',
    'network b:1:22:b::/64',
    'network b22::1/128',
    'exit',
    'exit'
]

i3_commands = [
    # --ipv6
    'ipv6 unicast-routing',
    
	'interface ethernet 1/1',
	'ipv6 add b:3:4:b::3/64',
	'exit',
 
    'interface ethernet 1/2',
	'ipv6 add b:1:2:b::3/64',
	'exit',
 
	'interface ethernet 1/3',
	'ipv6 add b:1:33:b::3/64',
	'exit',

    'interface loopback 3',
    'ipv6 add b33::1/128',
    'exit',
    
    'router bgp 3',
    'neigh b:3:4:b::5 remote-as 45',
    'neigh b:1:2:b::2 remote-as 2',
    'neigh b:1:33:b::1 remote-as 1',
    'address-family ipv6',
    'neigh b:3:4:b::5 activate',
    'neigh b:1:2:b::2 activate',
    'neigh b:1:33:b::1 activate',
    'network b:3:4:b::/64',
    'network b:1:2:b::/64',
    'network b:1:33:b::/64',
    'network b33::1/128',
    'exit',
    'exit'
]

i4_commands = [
    # --ipv6
    'ipv6 unicast-routing',
    
    'interface loopback 8',
    'ipv6 add 2001:4860:4860::8888/128',
    'exit',
    
    'interface ethernet 0/1',
    'ipv6 add b:1:4:b::5/64',
    'exit',
    
    'interface ethernet 0/2',
    'ipv6 add b:2:4:b::5/64',
    'exit',
    
    'interface ethernet 0/3',
    'ipv6 add b:3:4:b::5/64',
    'exit',
    
    'interface loopback 4',
	'ipv6 add b55::1/128',
    'exit',
    
	'router bgp 45',
    'neigh b:3:4:b::3 remote-as 3',
	'neigh b:2:4:b::2 remote-as 2',
	'neigh b:1:4:b::4 remote-as 45',
	'address-family ipv6',
    'neigh b:3:4:b::3 activate',
    'neigh b:2:4:b::2 activate',
    'neigh b:1:4:b::4 activate',
    'network b55::1/128',
    'network 2001:4860:4860::8888/128',
    'network b:3:4:b::/64',
    'network b:2:4:b::/64',
    'network b:1:4:b::/64',
    'exit',
    'exit'
]

r1_commands = [
    # --ipv6
    'ipv6 unicast-routing',
    
	'interface ethernet 1/3',
	'ipv6 add b:1:33:b::1/64',
    'exit',
    
	'interface ethernet 1/2',
	'ipv6 add b:1:22:b::1/64',
    'exit',
    
	'interface ethernet 1/1',
	'ipv6 add b:1:11:b::1/64',
    'exit',
    
    'router bgp 1',
    'neigh b:1:33:b::3 remote-as 3',
    'neigh b:1:22:b::2 remote-as 2',
    'neigh b:1:11:b::4 remote-as 45',
    'address-family ipv6',
    'neigh b:1:33:b::3 activate',
    'neigh b:1:22:b::2 activate',
    'neigh b:1:11:b::4 activate',
    'network FEC0:1::/122',
    'network b:1:33:b::/64',
    'network b:1:22:b::/64',
    'network b:1:11:b::/64',
    'exit',
    'exit',
    
    'interface Loopback 1',
    'ip address 1.1.1.1 255.255.255.255',
    'ipv6 address FEC0:1::1/122',
    'description Test I/F for BGP, OSPFv2 & OSPFv3 Routing',
    'exit',
    
    'interface ethernet 1/0',
    'ipv6 address 2026::12:1/122',
    'exit',
    
    # --ipv6 ospf config
    'ipv6 router ospf 6',
    'router-id 1.1.1.1',
    'exit',
    
    'interface loopback 1',
    'ipv6 ospf 6 area 12',
    'exit',
    
    'interface ethernet 1/0',
    'ipv6 ospf 6 area 12',
    'exit',
    
    # --ipv6 bgp-ospf redistribution
    'ipv6 router ospf 6',
    'default-information originate always',
    'redistribute bgp 1 metric 69',
    'exit',
    
    'router bgp 1',
    'address-family ipv6 unicast',
    'redistribute ospf 6 match internal external 1 external 2 include-connected',
    'exit'
]

r2_commands = [
    # --ipv6
    'ipv6 unicast-routing',
    
    'interface Loopback 2',
    'ip address 2.2.2.2 255.255.255.255',
    'ipv6 address FEC0:2::2/122',
    'description Test I/F for OSPFv2 & OSPFv3 Routing',
    'exit',
    
    'interface ethernet 1/2',
    'ipv6 address 2026::12:2/122',
    'exit',
    
    'interface ethernet 1/1',
    'ipv6 address 2026::1:1/122',
    'exit',
    
    # --ipv6 ospf config
    'ipv6 router ospf 6',
    'router-id 2.2.2.2',
    'exit',
    
    'interface loopback 2',
    'ipv6 ospf 6 area 0',
    'exit',
    
    'interface ethernet 1/1',
    'ipv6 ospf 6 area 0',
    'exit',
    
    'interface ethernet 1/2',
    'ipv6 ospf 6 area 12',
    'exit'
]

r3_commands = [
    # --ipv6
    'ipv6 unicast-routing',
    
    'interface Loopback 3',
    'ip address 3.3.3.3 255.255.255.255',
    'ipv6 address FEC0:3::3/122',
    'description Test I/F for OSPFv2 & OSPFv3 Routing',
    'exit',
    
    'interface Tunnel34',
    'no ip address',
    'ipv6 address 2026::34:1/122',
    'tunnel source lo3',
    'tunnel destination 4.4.4.4',
    'tunnel mode ipv6ip',
    'exit',
    
    'interface ethernet 1/1',
    'ipv6 address 2026::1:2/122',
    'exit',
    
    # --ipv6 ospf config
    'ipv6 router ospf 6',
    'router-id 3.3.3.3',
    'exit',
    
    'interface loopback 3',
    'ipv6 ospf 6 area 0',
    'exit',
    
    'interface Tunnel34',
    'ipv6 ospf 6 area 34',
    'exit',
    
    'interface ethernet 1/1',
    'ipv6 ospf 6 area 0',
    'exit'
]

r4_commands = [
    # --ipv6
    'ipv6 unicast-routing',
    
    'interface Loopback 4',
    'ip address 4.4.4.4 255.255.255.255',
    'ipv6 address FEC0::4:4/122',
    'description Test I/F for OSPFv2 & OSPFv3 Routing',
    'exit',
    
    'interface ethernet 1/0',
    'ip address 10.1.4.5 255.255.255.252',
    'ipv6 address 2026::2:1/122',
    'description L3 Link to DSW1',
    'exit',
    
    'interface ethernet 1/1',
    'ip address 10.1.4.9 255.255.255.252',
    'description L3 Link to DSW2 fa0/14',
    'exit',
    
    'interface Loopback 14',
    'no ip address',
    'ipv6 address FEC0::14:4/122',
    'description Test I/F for RIPng Routing',
    'exit',
    
    'interface Loopback 21',
    'ip address 10.1.21.129 255.255.255.224',
    'description Test I/F for EIGRPv4 Routing & IP(v4) Helper Loopback I/F',
    'exit',
    
    'interface Tunnel34',
    'no ip address',
    'ipv6 address 2026::34:2/122',
    'tunnel source loopback 4',
    'tunnel destination 3.3.3.3',
    'tunnel mode ipv6ip',
    'exit',
    
    # --ipv6 ospf config
    'ipv6 router ospf 6',
    'router-id 4.4.4.4',
    'exit',
    
    'interface loopback 4',
    'ipv6 ospf 6 area 34',
    'exit',
    
    'interface Tunnel34',
    'ipv6 ospf 6 area 34',
    'exit',
    
    # --ipv6 internal
    'interface ethernet 1/0',
    'ipv6 add 10:1:4:14::4/64',
    'exit',
    
    'interface ethernet 1/1',
    'ipv6 add 10:1:4:24::4/64',
    'exit',
    
    # --ipv6 eigrp config
    'ipv6 router eigrp 10',
    'eigrp router-id 4.4.4.4',
    'no shut',
    'exit',
    
    'interface loopback 4',
    'ipv6 eigrp 10',
    'exit',
    
    'interface ethernet 1/0',
    'ipv6 eigrp 10',
    'exit',
    
    'interface ethernet 1/1',
    'ipv6 eigrp 10',
    'exit',
    
    # --ipv6 eigrp-ospf redistribution
    'ipv6 router ospf 6',
    'redistribute eigrp 10 include-connected',
    'exit',
    
    'ipv6 router eigrp 10',
    'redistribute ospf 6 metric 10000 100 255 1 1500 include-connected',
    'exit'
]

r5_commands = [

]

r6_commands = [
    
]

d1_commands = [
    # --ipv6 internal
    'ipv6 unicast-routing',
    
    'interface Loopback 1',
    'ip address 11.11.11.11 255.255.255.255',
    'ipv6 address 11:11:11:11::1/128',
    'ipv6 address FEC0::11:1/122',
    'description IPv4, IPv6 & RIPng Test I/F',
    'exit',
    
    'interface ethernet 1/1',
    'no switchport',
    'ip address 10.1.4.6 255.255.255.252',
    'ipv6 address 2026::2:2/122',
    'ipv6 add 10:1:4:14::1/64',
    'description L3 UpLink to R4',
    'exit',
    
    'interface vlan 200',
    'ipv6 address 2026::3:1/122',
    'ipv6 add 192:168:1:1234::1/64',
    'description IPv6 Link to DSW2',
    'exit',
    
    'int vlan 10',
    'ipv6 add 10:2:1:12::1/64',
    'exit',
    
    'int vlan 20',
    'ipv6 add 10:2:2:12::1/64',
    'exit',
    
    # --ipv6 eigrp config
    'interface loopback 1',
    'ipv6 address 11:11:11:11::1/64',
    'ipv6 router eigrp 10',
    'eigrp router-id 1.1.1.1',
    'no shut',
    'exit',
    
    'interface lo1',
    'ipv6 eigrp 10',
    'exit',
    
    'interface e1/1',
    'ipv6 eigrp 10',
    'exit',
    
    'interface vlan 10',
    'ipv6 eigrp 10',
    'exit',
    
    'interface vlan 20',
    'ipv6 eigrp 10',
    'exit',
    
    'interface vlan 200',
    'ipv6 eigrp 10',
    'exit'
]

d2_commands = [
    # --ipv6 internal
    'ipv6 unicast-routing',
    
    'interface Loopback 2',
    'ip address 22.22.22.22 255.255.255.255',
    'ipv6 add 22:22:22:22::2/128',
    'ipv6 address FEC0::22:2/122',
    'description IPv4, IPv6 & RIPng Test I/F',
    'exit',
    
    'interface ethernet 1/1',
    'ipv6 add 10:1:4:24::2/64',
    'exit',
    
    'interface vlan 200',
    'ipv6 address 2026::3:2/122',
    'ipv6 add 192:168:1:1234::2/64',
    'description IPv6 Link to DSW1',
    'exit',
    
    'interface vlan 10',
    'ipv6 add 10:2:1:12::2/64',
    'exit',
    
    'interface vlan 20',
    'ipv6 add 10:2:2:12::2/64',
    'exit',
    
    # --ipv6 eigrp config
    'interface loopback 1',
    'ipv6 address 22:22:22:22::2/64',
    'ipv6 router eigrp 10',
    'eigrp router-id 2.2.2.2',
    'no shut',
    'exit',
    
    'interface loopback 1',
    'ipv6 eigrp 10',
    'exit',
    
    'interface ethernet 1/1',
    'ipv6 eigrp 10',
    'exit',
    
    'interface vlan 10',
    'ipv6 eigrp 10',
    'exit',
    
    'interface vlan 20',
    'ipv6 eigrp 10',
    'exit',
    
    'interface vlan 200',
    'ipv6 eigrp 10',
    'exit'
]

a1_commands = [
]

a2_commands = [
]

s1_commands = [
]

s2_commands = [
]

p1_commands = [
    # --ipv6
    'ipv6 unicast-routing',
    
    'interface ethernet 0/0',
    'ipv6 en',
    'ipv6 add 10:2:1:12::B00B/64',
    'ipv6 add autoconfig',
    'exit',
    
    'ipv6 route ::/0 10:2:1:12::1'
    
]

p2_commands = [
    # --ipv6
    'ipv6 unicast-routing',
    
    'ipv6 route ::/0 10:2:1:12::2',
    
    'interface ethernet 1/0',
    'ipv6 address 10:2:1:12::/64 eui-64',
    'exit',
    
    'ipv6 route ::/0 10:2:1:12::2'
]
