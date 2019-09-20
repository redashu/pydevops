#!/usr/bin/python3

import paramiko,time

#  using ssh client library 
client=paramiko.SSHClient()
#print(dir(client))  #  to explore library or variable 
# adding  line for ignoring  host key 
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#  now we can connect with device
ip="192.168.122.131"
username='root'
password='cisco'
client.connect(ip,
        username=username,
        password=password,
        allow_agent=False,
        look_for_keys=False)
#  calling  shell
device_shell=client.invoke_shell()
#  run command
#print(dir(device_shell))
#  now using  sending  method to send commands
device_shell.send("sh run\n".encode('ascii'))
time.sleep(2)
output=device_shell.recv(65000)
print(output.decode('ascii'))


