#!/usr/bin/python3

import time

print(" Iam Started..")
s=0
while 1:
   s=s+1
   time.sleep(1)
   if s%2==0:
       print("total seconds",s)
