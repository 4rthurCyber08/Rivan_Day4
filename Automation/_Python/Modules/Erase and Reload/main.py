
from netmiko import ConnectHandler

list_of_device = input('What devices do you want to reload? [ex. 10.12.1.2 10.12.1.4] ')
list_of_device = list_of_device.split()

### Device Information
device_info = {
    'device_type': 'cisco_ios_telnet',
    'host': '10.#$34T#.1.2',
    'username': 'admin',
    'password': 'pass',
    'secret': 'pass',
    'port': 23
}

for host in list_of_device:
    device_info['host'] = host
    
    try:
        ### Connect to Device
        access_cli = ConnectHandler(**device_info)
        access_cli.enable()
        
        print(f'Accessing {host} \n')
        ### Delete Start Config
        output = access_cli.send_command_timing('write erase')
        if 'Continue?' in output:
            output += access_cli.send_command_timing('\n')
        
        print(output)
        
        ### Reload Device
        output = access_cli.send_command_timing('reload')
        if 'Save?' in output:
            output += access_cli.send_command_timing('No')
        if 'Proceed with reload?' in output:
            output += access_cli.send_command_timing('\n')
            
        print(output)

        ### Close Connection
        access_cli.disconnect()
        
        print(f'\n\n Closing connection to {host} \n')
        
    except Exception as e:
        print(f'''
Failed to Connect to Device: {host}:
Reason for failure: 
{e}

              ''')
