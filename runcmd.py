#!/usr/bin/python3


import  subprocess

#  to input from user 

x=input("please enter any command to run :-->>   ")

out=subprocess.getoutput(x)
print("@@@@@@@@@@@@@@@@@@@@@@")
print("@@                 @@")
print("@@                 @@@")
print("@@                 @@")
print(out)

