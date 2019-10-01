#!/usr/bin/python3

import netmiko

device={
        
        'device_type' : 'cisco_ios',
        'username' : 'root',
        'password' : 'cisco',
        'host' : '192.168.122.138',
        'port' :  22
        
        }

try : 

#  now connection with device
    device_connect=netmiko.ConnectHandler(**device)
    print(device_connect)
    #  running  command in  privilage  
    #output=device_connect.send_command("show ip int br")
    #output=device_connect.send_config_set("hostname  helloadhoc")
    output=device_connect.send_config_from_file("abc.txt")
    print(output)


except    ValueError:
    print("plz check your device type  value : ")

except netmiko.ssh_exception.NetMikoAuthenticationException: 
    print("plz check your username or password ")

except  netmiko.ssh_exception.NetMikoTimeoutException:
    print("Plz check your Device  IP ")

except   :
    print("hey i think you need to check your code values ")
