#!/usr/bin/python3
import sys
   
for line in sys.stdin:
    temp = line.split()
    print(temp[0],",",temp[1])

