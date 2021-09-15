#!/usr/bin/env python

import sys
state_city=set()
cityCount= dict()
prevstate=None
statecount=0

def printcity():
    for city in cityCount.keys():
        print(city,cityCount[city])

for line in sys.stdin:
    state, city, count = line.split(",")

    try:
        count = int(count)
    except ValueError:
        continue
	
    if city not in cityCount.keys():
        cityCount[city] = 0
    cityCount[city]+=count
    statecount+=count

    if(prevstate == None):
      continue
    elif(prevstate != state):
      print(prevstate)
      printcity()
      print(statecount)
      statecount=0
    
    prevstate=state




	
