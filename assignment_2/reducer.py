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
    state, city, count = line.split(",").strip()

    try:
        count = int(count)
    except ValueError:
        continue

	
    if(prevstate==None):
        if city not in cityCount.keys():
            cityCount[city] = 0
        cityCount[city]+=count
        statecount+=count
        prevstate=state
        continue
    elif(prevstate != state):
      print(prevstate)
      printcity()
      print(prevstate,statecount)
      statecount=0
      cityCount.clear()

    if city not in cityCount.keys():
        cityCount[city] = 0
    cityCount[city]+=count
    statecount+=count
    
    prevstate=state

print(prevstate)
printcity()
print(prevstate,statecount)
statecount=0




