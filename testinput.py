#!/usr/bin/python3

import  sys
#x=input("enter command : ")

y=sys.argv[1:]
cmd=""
for  i in  y:
    cmd=cmd+" "+i


print(cmd+"\n")
