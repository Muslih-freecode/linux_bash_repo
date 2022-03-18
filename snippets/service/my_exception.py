#!/usr/bin/python3

import time

print(" Iam Started..")
s=0
while 1:
   s=s+1
   time.sleep(1)
   if s%2==0:
       print("total seconds",s)
   if s%3==0:
       raise Exception("Sorry, no numbers below zero")
