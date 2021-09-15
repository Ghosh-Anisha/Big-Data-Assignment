#!/usr/bin/env python

import sys
state_city=list()
cityCount= dict()

for line in sys.stdin:
    state, city, count = line.split(",")
    # state=obj["state"]
    # city=obj["city"]
    
    try:
        count = int(count)
    except ValueError:
        continue
	
    if city not in cityCount.keys():
        cityCount[city] = 0
    cityCount[city]+= count
    
    if city not in state_city:
    	state_city.append((state,city))
	
for (state, city) in state_city:
	acc=0
	print(state)
	for city1 in sorted(cityCount.keys()):
		if (city1 == city):
			print("{}\t{}".format(city1,cityCount[city]))
		acc+=cityCount[city]
	print(state, acc)
	
