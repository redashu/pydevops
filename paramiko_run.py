#!/usr/bin/python3

import paramiko,time
import  sys
data=sys.argv[1:]
cmd=""
for i in data:
    cmd=cmd+" "+i

newcmd=cmd+"\n"
#  using ssh client library 
client=paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ip=["192.168.122.131","192.168.122.138"]

username='root'
password='cisco'

for  i   in  ip:
    print("Connecting to Device  :  ",i)
    print("_________________________")
    print("_________________________")
    client.connect(i,username=username,password=password,allow_agent=False,look_for_keys=False)
#  calling  shell
    device_shell=client.invoke_shell()
#  run command
#print(dir(device_shell))
#  now using  sending  method to send commands
    device_shell.send(newcmd.encode('ascii'))
    time.sleep(2)
    output=device_shell.recv(65000)
    print(output.decode('ascii'))
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    print("@@                      @@@@")
    print("_________________________")


