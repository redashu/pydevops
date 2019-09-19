#!/usr/bin/python3

import  hello,time,subprocess

print("hiiiiiiiiiiiiii")
time.sleep(2)    #  it will pause the program for 5 seconds 
print("hello world")

'''
x=pyttsx3.init()   #  load sound drive in python 
x.say("hello world")
x.runAndWait()  

'''
#  to run linux or windows / mac command use subprocess module
y=subprocess.getoutput("date")
print(y)







