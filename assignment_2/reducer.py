#!/usr/bin/env python

import sys
citycount= 0
prevstate=None
prevcity=None
statecount=0


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
        print(prevstate,statecount)
        statecount=0
      print(state)
      prevstate=state
    if(prevstate==state):
        if(prevcity != city):
            #print(prevcity,city)
            if(prevcity != None):
                print(prevcity,citycount)
                citycount=0
            prevcity=city     
        citycount+=count
        statecount+=count
print(prevstate,statecount)


