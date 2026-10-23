from json import load

# read json file
with open('pre_config.json') as file:
    # convert json data types to python data types
    json_configs = load(file)

# parse device configs
dhcp = json_configs['dhcp_config']
ip = json_configs['i_protocol']
eigrp = json_configs['eigrp_config']
ospf = json_configs['ospf_config']
bgp = json_configs['bgp_config']
p2_config = json_configs['p2_config']
p1_config = json_configs['p1_config']
a2_config = json_configs['a2_config']
a1_config = json_configs['a1_config']
d2_config = json_configs['d2_config']
d1_config = json_configs['d1_config']
s1_config = json_configs['s1_config']
s2_config = json_configs['s2_config']
r4_config = json_configs['r4_config']
r3_config = json_configs['r3_config']
r2_config = json_configs['r2_config']
r1_config = json_configs['r1_config']
i1_config = json_configs['i1_config']
i2_config = json_configs['i2_config']
i3_config = json_configs['i3_config']
i4_config = json_configs['i4_config']
r5_config = json_configs['r5_config']
r6_config = json_configs['r6_config']

# commands to be pushed to cli
i1_commands = [
    # bgp config
    f'router {bgp["as_34"]}',
    'bgp log-neighbor-changes',
    f'{i1_config["neigh_45"]}',
    f'{i1_config["neigh_24"]}',
    f'{i1_config["neigh_208"]}',
    f'{bgp["ipv4_fam"]}',
    f'{i1_config["neigh_45_on"]}',
    f'{i1_config["neigh_24_on"]}',
    f'{i1_config["neigh_208_on"]}',
    f'network {i1_config["lo0"]} mask {ip["mask_32"]}',
    f'network {bgp["net_45"]} mask {ip["mask_24"]}',
    f'network {bgp["net_24"]} mask {ip["mask_24"]}',
    f'network {bgp["net_208"]} mask {ip["mask_24"]}',
    'exit',
    'exit',
]

i2_commands = [
    # bgp config
    f'router {bgp["as_25"]}',
    'bgp log-neighbor-changes',
    f'{i2_config["neigh_32"]}',
    f'{i2_config["neigh_25"]}',
    f'{i2_config["neigh_24"]}',
    f'{i2_config["neigh_207"]}',
    f'{bgp["ipv4_fam"]}',
    f'{i2_config["neigh_32_on"]}',
    f'{i2_config["neigh_25_on"]}',
    f'{i2_config["neigh_24_on"]}',
    f'{i2_config["neigh_207_on"]}',
    f'network {i2_config["lo0"]} mask {ip["mask_32"]}',
    f'network {bgp["net_32"]} mask {ip["mask_24"]}',
    f'network {bgp["net_25"]} mask {ip["mask_24"]}',
    f'network {bgp["net_24"]} mask {ip["mask_24"]}',
    'exit',
    'exit',
]

i3_commands = [
    # bgp config
    f'router {bgp["as_34"]}',
    'bgp log-neighbor-changes',
    f'{i3_config["neigh_35"]}',
    f'{i3_config["neigh_32"]}',
    f'{i3_config["neigh_209"]}',
    f'{bgp["ipv4_fam"]}',
    f'{i3_config["neigh_35_on"]}',
    f'{i3_config["neigh_32_on"]}',
    f'{i3_config["neigh_209_on"]}',
    f'network {i3_config["lo0"]} mask {ip["mask_32"]}',
    f'network {bgp["net_35"]} mask {ip["mask_24"]}',
    f'network {bgp["net_32"]} mask {ip["mask_24"]}',
    f'network {bgp["net_209"]} mask {ip["mask_24"]}',
    'exit',
    'exit',
]

i4_commands = [
    # bgp config
    f'router {bgp["as_25"]}',
    'bgp log-neighbor-changes',
    f'{i4_config["neigh_35"]}',
    f'{i4_config["neigh_25"]}',
    f'{i4_config["neigh_45"]}',
    f'{bgp["ipv4_fam"]}',
    f'{i4_config["neigh_35_on"]}',
    f'{i4_config["neigh_25_on"]}',
    f'{i4_config["neigh_45_on"]}',
    f'network {i4_config["google"]} mask {ip["mask_32"]}',
    f'network {i4_config["lo0"]} mask {ip["mask_32"]}',
    f'network {bgp["net_35"]} mask {ip["mask_24"]}',
    f'network {bgp["net_25"]} mask {ip["mask_24"]}',
    f'network {bgp["net_45"]} mask {ip["mask_24"]}',
    'exit',
    'exit',
]

r1_commands = [
    # ospf config
    f'router ospf {ospf["process_id"]}',
    f'router-id {r1_config["r_id"]}',
    f'network {ospf["net_1_0"]}',
    f'network {r1_config["r_id"]} 0.0.0.0 area 12',
    'passive-interface lo1',
    f'{ospf["redis_bgp"]} always',
    f'auto-cost reference-bandwidth {ospf["ref-bw"]}',
    'exit',

    # int priority
    'int e1/0',
    'ip ospf priority 0',

    # 'ip route 0.0.0.0  0.0.0.0  207.7.7.2  7',
    # 'ip route 0.0.0.0  0.0.0.0  208.8.8.4  8',
    # 'ip route 0.0.0.0  0.0.0.0  209.9.9.3  9',

    # nat
    'int e1/0',
    'ip nat inside',
    'int range e1/1-3',
    'ip nat outside',

    # nat traffic
    'access-list 1 permit 10.0.0.0     0.255.255.255',
    'access-list 1 permit 172.16.0.0   0.15.255.255',
    'access-list 1 permit 192.168.0.0  0.0.255.255',
    
    # nat pool
    'ip nat pool POOL7 207.7.7.10 207.7.7.254 netmask 255.255.255.0',
    'ip nat pool POOL8 208.8.8.10 208.8.8.254 netmask 255.255.255.0',
    'ip nat pool POOL9 209.9.9.10 209.9.9.254 netmask 255.255.255.0',

    # nat route-map
    'route-map PBR_CONVERGE permit 10',
    'match ip address 1',
    'match interface e1/1',
    'route-map PBR_PLDT permit 10',
    'match ip address 1',
    'match interface e1/2',
    'route-map PBR_GLOBE permit 10',
    'match ip address 1',
    'match interface e1/3',
    
    # pat
    'ip nat inside source route-map PBR_CONVERGE pool POOL8 overload',
    'ip nat inside source route-map PBR_PLDT pool POOL7 overload',
    'ip nat inside source route-map PBR_GLOBE pool POOL9 overload',

    # bgp config
    f'router {bgp["as_1"]}',
    'bgp log-neighbor-changes',
    f'{r1_config["neigh_209"]}',
    f'{r1_config["neigh_207"]}',
    f'{r1_config["neigh_208"]}',
    f'{bgp["ipv4_fam"]}',
    f'{r1_config["neigh_209_on"]}',
    f'{r1_config["neigh_207_on"]}',
    f'{r1_config["neigh_208_on"]}',
    f'network {bgp["net_209"]} mask {ip["mask_24"]}',
    f'network {bgp["net_207"]} mask {ip["mask_24"]}',
    f'network {bgp["net_208"]} mask {ip["mask_24"]}',
    'exit',
    'exit'
]

r2_commands = [
    # ospf config
    f'router ospf {ospf["process_id"]}',
    f'router-id {r2_config["r_id"]}',
    f'network {ospf["net_1_4"]}',
    f'network {ospf["net_1_0"]}',
    f'network {ospf["net_2_4"]}',
    f'network {ospf["net_2_12"]}',
    f'network {ospf["net_3_4"]}',
    f'network {r2_config["r_id"]} 0.0.0.0 area 0',
    'passive-interface lo2',
    f'auto-cost reference-bandwidth {ospf["ref-bw"]}',
    'area 352 stub no-summary',
    'exit',
    'ip route 4.4.4.4 255.255.255.255 10.1.1.6',
    # int priority
    'int e1/2',
    'ip ospf priority 255',
    'exit'

]

r3_commands = [
    # ospf config
    f'router ospf {ospf["process_id"]}',
    f'router-id {r3_config["r_id"]}',
    f'network {ospf["net_1_8"]}',
    f'network {ospf["net_1_4"]}',
    f'network {ospf["net_2_4"]}',
    f'network {ospf["net_2_8"]}',
    f'network {r3_config["r_id"]} 0.0.0.0 area 0',
    'passive-interface lo3',
    f'auto-cost reference-bandwidth {ospf["ref-bw"]}',
    'area 352 stub no-summary',
    'area 34 nssa no-summary',
    'exit'
]

r4_commands = [
    # eigrp config
    f'router eigrp {eigrp["named-eigrp"]}',
    f'address-family ipv4 unicast autonomous-system {eigrp["as100"]}',
    f'network {eigrp["net_4_4"]}',
    f'network {eigrp["net_4_8"]}',
    f'network {eigrp["net_8_4"]}',
    f'network {eigrp["net_8_8"]}',
    'af-interface e1/0',
    'passive-interface',
    'topology base',
    f'{eigrp["redis_ospf_1"]}',
    'no auto-summary',
    'exit',
    'exit',
    
    # ospf config
    f'router ospf {ospf["process_id"]}',
    f'router-id {r4_config["r_id"]}',
    f'network {ospf["net_1_8"]}',
    f'network {r4_config["r_id"]} 0.0.0.0 area 34',
    'passive-interface lo4',
    f'auto-cost reference-bandwidth {ospf["ref-bw"]}',
    'area 34 nssa',
    f'{ospf["redis_eigrp_100"]}',
    'exit',

    # ospf p2p
    'int e1/2',
    'ip ospf hello-interval 15',
    'ip ospf dead-interval 60',
    'ip ospf network point-to-point',
    'exit',

    'int e2/0',
    'no shut',
    'ip add 10.1.8.5 255.255.255.252',
    'exit',
    'int e2/1',
    'no shut',
    'ip add 10.1.8.9 255.255.255.252',
    'exit',
]

d1_commands = [
    'vlan 51',
    'name GUESTS',
    'exit',
    'int vlan 51',
    'no shut',
    'ip add 10.1.51.1 255.255.255.0',
    'bandwidth 100',
    'delay 1000',
    'exit',
    
    'int e2/0',
    'no sw',
    'no shut',
    'ip add 10.1.8.6 255.255.255.252',
    'exit',


    'int e1/0',
    'no shut',
    'switchport trunk encaps dot1q',
    'switchport mode trunk',
    'switchport trunk allowed vlan 100',
    'exit',


    # eigrp config
    f'router eigrp {eigrp["named-eigrp"]}',
    f'address-family ipv4 unicast autonomous-system {eigrp["as100"]}',
    f'eigrp router-id {d1_config["r_id"]}',
    f'network {eigrp["net_4_4"]}',
    f'network {eigrp["net_1_0"]}',
    f'network {eigrp["net_2_0"]}',
    f'network {eigrp["net_8_4"]}',
    f'network {eigrp["net_v100"]}',
    f'network {eigrp["net_51"]}',
    'af-interface e1/0',
    'passive-interface',
    'exit',
    'exit'
]

d2_commands = [
    'vlan 51',
    'name GUESTS',
    'exit',
    'int vlan 51',
    'no shut',
    'ip add 10.1.51.2 255.255.255.0',
    'bandwidth 100',
    'delay 1000',
    'exit',

    'int e2/1',
    'no sw',
    'no shut',
    'ip add 10.1.8.10 255.255.255.252',
    'exit',

    'int e1/0',
    'no shut',
    'switchport mode access',
    'switchport access vlan 20',
    'exit',

    # eigrp config
    f'router eigrp {eigrp["named-eigrp"]}',
    f'address-family ipv4 unicast autonomous-system {eigrp["as100"]}',
    f'eigrp router-id {d2_config["r_id"]}',
    f'network {eigrp["net_4_8"]}',
    f'network {eigrp["net_1_0"]}',
    f'network {eigrp["net_2_0"]}',
    f'network {eigrp["net_8_8"]}',
    f'network {eigrp["net_v100"]}',
    f'network {eigrp["net_51"]}',
    'af-interface e1/0',
    'passive-interface',
    'exit',
    'exit'
]

a1_commands = [
    'vlan 49',
    'name FINANCE',
    'vlan 51',
    'name GUESTS',
    'exit',
    'int vlan 49',
    'no shut',
    'ip add 10.1.49.1 255.255.255.0',
    'bandwidth 10000000',
    'delay 1000',
    'exit',
    'int vlan 51',
    'no shut',
    'ip add 10.1.51.3 255.255.255.0',
    'bandwidth 1000',
    'delay 100',
    'exit',

    'int e0/0',
    'no shut',
    'switchport mode access',
    'switchport access vlan 10',
    'exit',
    
    # eigrp config
    f'router eigrp {eigrp["named-eigrp"]}',
    f'address-family ipv4 unicast autonomous-system {eigrp["as100"]}',
    f'network {eigrp["net_v100"]}',
    f'network {eigrp["net_49"]}',
    f'network {eigrp["net_51"]}',
    'af-interface e0/0',
    'passive-interface',
    'exit',
    'exit'
]

a2_commands = [
    'vlan 50',
    'name SOC',
    'vlan 51',
    'name GUESTS',
    'exit',
    'int vlan 50',
    'no shut',
    'ip add 10.1.50.1 255.255.255.0',
    'bandwidth 1000',
    'delay 500',
    'exit',
    'int vlan 51',
    'no shut',
    'ip add 10.1.51.4 255.255.255.0',
    'bandwidth 10000',
    'delay 10',
    'exit',

    'int e1/0',
    'no shut',
    'switchport mode access',
    'switchport access vlan 10',
    'exit',

    # eigrp config
    f'router eigrp {eigrp["named-eigrp"]}',
    f'address-family ipv4 unicast autonomous-system {eigrp["as100"]}',
    f'network {eigrp["net_v100"]}',
    f'network {eigrp["net_50"]}',
    f'network {eigrp["net_51"]}',
    'af-interface e1/0',
    'passive-interface',
    'exit',
    'exit'
]

s1_commands = [
    'interface e1/0',
    'no shutdown',
    f'ip add {s1_config["int_1_0"]} {ip["mask_27"]}',
    'exit',
    
    f'ip route {ip["def_route"]} {s1_config["gateway_1"]}',
    f'ip route {ip["def_route"]} {s1_config["gateway_2"]} 10'
]

s2_commands = [
    'interface e1/0',
    'no shutdown',
    f'ip add {s2_config["int_1_0"]} {ip["mask_24"]}',
    'exit',
]

p1_commands = [
    f'ip route {ip["def_route"]} {ip["def_1_1"]} 1',
    f'ip route {ip["def_route"]} {ip["def_1_2"]} 10',
    
    'interface ethernet 0/0',
    'ip add 10.2.1.101 255.255.255.0',
    'no shutdown',
    'exit'
]

p2_commands = [    
    f'ip route {ip["def_route"]} {ip["def_1_2"]} 1',
    f'ip route {ip["def_route"]} {ip["def_1_1"]} 10',

    'interface ethernet 1/0',
    'ip add 10.2.1.102 255.255.255.0',
    'no shutdown',
    'exit'
]

r5_commands = [
    # ospf config
    f'router ospf {ospf["process_id"]}',
    f'router-id {r5_config["r_id"]}',
    f'network {ospf["net_2_12"]}',
    f'network {ospf["net_2_8"]}',
    f'network {r5_config["r_id"]} 0.0.0.0 area 352',
    'passive-interface lo5',
    f'auto-cost reference-bandwidth {ospf["ref-bw"]}',
    'area 352 stub',
    'exit'
]

r6_commands = [
    'int lo10',
    'ip add 10.6.144.6 255.255.255.0',
    'ip ospf 1 area 26',
    'int lo11',
    'ip add 10.6.157.6 255.255.255.0',
    'ip ospf 1 area 26',
    'int lo12',
    'ip add 10.6.159.6 255.255.255.0',
    'ip ospf 1 area 26',
    'int lo13',
    'ip add 10.6.171.6 255.255.255.0',
    'ip ospf 1 area 26',
    'int lo14',
    'ip add 10.6.180.6 255.255.255.128',
    'ip ospf 1 area 26',
    'int lo15',
    'ip add 10.6.180.166 255.255.255.128',
    'ip ospf 1 area 26',
    'int lo16',
    'ip add 10.26.22.6 255.255.254.0',
    'ip ospf 1 area 26',
    'int lo17',
    'ip add 10.26.29.6 255.255.255.0',
    'ip ospf 1 area 26',
    'int lo18',
    'ip add 10.26.34.6 255.255.252.0',
    'ip ospf 1 area 26',
    'int lo19',
    'ip add 10.26.41.6 255.255.255.128',
    'ip ospf 1 area 26',
    'int lo20',
    'ip add 10.26.47.206 255.255.255.192',
    'ip ospf 1 area 26',
    'exit',
    'int range lo10-20',
    'ip ospf network point-to-point',
    'exit',

    # ospf config
    f'router ospf {ospf["process_id"]}',
    f'router-id {r6_config["r_id"]}',
    f'network {ospf["net_3_4"]}',
    f'network {ospf["net_3_0"]}',
    f'network {r6_config["r_id"]} 0.0.0.0 area 26',
    'passive-interface lo6',
    'passive-interface lo10',
    'passive-interface lo11',
    'passive-interface lo12',
    'passive-interface lo13',
    'passive-interface lo14',
    'passive-interface lo15',
    'passive-interface lo16',
    'passive-interface lo17',
    'passive-interface lo18',
    'passive-interface lo19',
    'passive-interface lo20',
    f'auto-cost reference-bandwidth {ospf["ref-bw"]}',
    'area 26 stub',
    'exit'
]
