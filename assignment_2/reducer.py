#! /usr/bin/env python3

import sys
citycount= 0
prevstate=None
prevcity=None
statecount=0
flag=0

for line in sys.stdin:
    state, city, count = line.split(",")
    state=state.strip()
    city=city.strip()
    city=city[:-1]
    count=count.strip()

    try:
        count = int(count)
    except ValueError:
        continue

    if(prevstate != state):
      if(prevstate != None):
        print(prevcity,citycount)
        print(prevstate,statecount)
        citycount=0
        flag=1
        statecount=0
      print(state)
      prevstate=state
    if(prevstate==state):
        if(prevcity != city):
            if(prevcity != None and flag!=1):
                print(prevcity,citycount)
                citycount=0
            prevcity=city
            flag=0     
        citycount+=count
        statecount+=count
print(prevcity,citycount)
print(prevstate,statecount)

