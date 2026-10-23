from json import load
from netmiko import ConnectHandler
from multiprocessing import Process
import ipv4_commands as ipv4
import ipv6_commands as ipv6
    
def configDeviceTelnet(device_info, script, sh_cli=True):
    '''
    This function handles connection and
    configuration of the device.
    '''
    accessCli = ConnectHandler(**device_info)
    accessCli.enable()
    output = accessCli.send_config_set(script)
    
    # accessCli.disconnect()
    
    if sh_cli:
        print(output)

def getDevicePort(device, device_info):
    '''
    This function will get 
    the port number of the device.
    '''
    
    if device == 'P1':
        device_info['port'] = 2361
    elif device == 'P2':
        device_info['port'] = 2362
    elif device == 'A1':
        device_info['port'] = 2363
    elif device == 'A2':
        device_info['port'] = 2364
    elif device == 'S1':
        device_info['port'] = 2365
    elif device == 'D1':
        device_info['port'] = 2366
    elif device == 'D2':
        device_info['port'] = 2367
    elif device == 'S2':
        device_info['port'] = 2368
    elif device == 'R4':
        device_info['port'] = 2369
    elif device == 'R3':
        device_info['port'] = 2370
    elif device == 'R2':
        device_info['port'] = 2371
    elif device == 'R1':
        device_info['port'] = 2372
    elif device == 'I3':
        device_info['port'] = 2373
    elif device == 'I2':
        device_info['port'] = 2374
    elif device == 'I1':
        device_info['port'] = 2375
    elif device == 'R5':
        device_info['port'] = 2376
    elif device == 'R6':
        device_info['port'] = 2377
    elif device == 'I4':
        device_info['port'] = 2378

    
    return device_info

def setConfigurationType(): 
    ip_type = input('What configurations should be applied? \nIPv4 ONLY = 1, Dualstack = 0\n ' )
    
    if ip_type == '1':
        ip_type = 'ipv4'
    else:
        ip_type = 'ipv6'
        
    return ip_type

def addIpv6Configs(script:list, ipv6_commands):
    '''
    This function will add ipv6 configurations
    to the ipv4 script.
    '''
    
    for command in ipv6_commands:
        script.append(command)
    
    return script

def main(device, 
         device_info, 
         script, 
         protocol='ipv4', 
         sh_cli=True):
        
    # get the port number of the device
    device_info = getDevicePort(device, device_info)
    
    # add ipv6 commands to the ipv4 script if specified
    if protocol == 'ipv6':

        # no ipv6 allowed
        print(' LOL IPV4 ONLY ')

        # if device == 'P1':
        #     script = addIpv6Configs(script, ipv6.p1_commands)
            
        # elif device == 'P2':
        #     script = addIpv6Configs(script, ipv6.p2_commands)
            
        # elif device == 'S1':
        #     script = addIpv6Configs(script, ipv6.s1_commands)
            
        # elif device == 'S2':
        #     script = addIpv6Configs(script, ipv6.s2_commands)
            
        # elif device == 'A1':
        #     script = addIpv6Configs(script, ipv6.a1_commands)
            
        # elif device == 'A2':
        #     script = addIpv6Configs(script, ipv6.a2_commands)
            
        # elif device == 'D1':
        #     script = addIpv6Configs(script, ipv6.d1_commands)
            
        # elif device == 'D2':
        #     script = addIpv6Configs(script, ipv6.d2_commands)
            
        # elif device == 'R4':
        #     script = addIpv6Configs(script, ipv6.r4_commands)
            
        # elif device == 'R3':
        #     script = addIpv6Configs(script, ipv6.r3_commands)
            
        # elif device == 'R2':
        #     script = addIpv6Configs(script, ipv6.r2_commands)
            
        # elif device == 'R1':
        #     script = addIpv6Configs(script, ipv6.r1_commands)
            
        # elif device == 'I1':
        #     script = addIpv6Configs(script, ipv6.i1_commands)
            
        # elif device == 'I2':
        #     script = addIpv6Configs(script, ipv6.i2_commands)
            
        # elif device == 'I3':
        #     script = addIpv6Configs(script, ipv6.i3_commands)
            
        # elif device == 'I4':
        #     script = addIpv6Configs(script, ipv6.i4_commands)

        # elif device == 'R5':
        #     script = addIpv6Configs(script, ipv6.r5_commands)

        # elif device == 'R6':
        #     script = addIpv6Configs(script, ipv6.r6_commands)
    
    print(f'Configuring...{device}')
    # establish connection then push configurations
    configDeviceTelnet(device_info, script, sh_cli)

if __name__ == '__main__':
    with open('device_info_temp.json') as file: 
        json_info = load(file)
    
    # unpack ConnectHandler arguments
    device_info = json_info['device_info']
    
    # get the ip address of the user's rstlab
    device_info['ip'] = input('What is the ip address of your \'RSTHayup Virtual Machine\'? ')
    
    # prompt user if configurations should be ipv4 only or Dualstack
    configuration_type = setConfigurationType()
    
    # set multiprocessing
    order_of_config = ['I4', 'I3', 'I2', 'I1', 'R1', 'R3', 'R2', 'R4', 'R5', 'R6', 'D1', 'D2', 'A1', 'A2', 'S1', 'P1', 'P2']
    process_list = []
    
    for device in order_of_config:
        if device == 'P1':
            instance = Process(target=main, args=[device, device_info, ipv4.p1_commands, configuration_type, True])
            
        elif device == 'P2':
            instance = Process(target=main, args=[device, device_info, ipv4.p2_commands, configuration_type, True])
            
        elif device == 'S1':
            instance = Process(target=main, args=[device, device_info, ipv4.s1_commands, configuration_type, True])
            
        #elif device == 'S2':
        #    instance = Process(target=main, args=[device, device_info, ipv4.s2_commands, configuration_type, True])
            
        elif device == 'A1':
            instance = Process(target=main, args=[device, device_info, ipv4.a1_commands, configuration_type, True])
            
        elif device == 'A2':
            instance = Process(target=main, args=[device, device_info, ipv4.a2_commands, configuration_type, True])
            
        elif device == 'D1':
            instance = Process(target=main, args=[device, device_info, ipv4.d1_commands, configuration_type, True])
            
        elif device == 'D2':
            instance = Process(target=main, args=[device, device_info, ipv4.d2_commands, configuration_type, True])
            
        elif device == 'R4':
            instance = Process(target=main, args=[device, device_info, ipv4.r4_commands, configuration_type, True])
            
        elif device == 'R3':
            instance = Process(target=main, args=[device, device_info, ipv4.r3_commands, configuration_type, True])
            
        elif device == 'R2':
            instance = Process(target=main, args=[device, device_info, ipv4.r2_commands, configuration_type, True])
            
        elif device == 'R1':
            instance = Process(target=main, args=[device, device_info, ipv4.r1_commands, configuration_type, True])
            
        elif device == 'I1':
            instance = Process(target=main, args=[device, device_info, ipv4.i1_commands, configuration_type, True])
            
        elif device == 'I2':
            instance = Process(target=main, args=[device, device_info, ipv4.i2_commands, configuration_type, True])
            
        elif device == 'I3':
            instance = Process(target=main, args=[device, device_info, ipv4.i3_commands, configuration_type, True])

        elif device == 'R5':
            instance = Process(target=main, args=[device, device_info, ipv4.r5_commands, configuration_type, True])

        elif device == 'R6':
            instance = Process(target=main, args=[device, device_info, ipv4.r6_commands, configuration_type, True])

        elif device == 'I4':
            instance = Process(target=main, args=[device, device_info, ipv4.i4_commands, configuration_type, True])
            
        process_list.append(instance)
    
    for process in process_list:
        process.start()
        
    for process in process_list:
        process.join()
    
    print(f'Configurations complete for : Clone of RSTallrun [{device_info["ip"]}]')
    print(r'Please wait for BGP to build routes before pinging 8.8.8.8')
    input(r'Press Enter to close terminal.')
