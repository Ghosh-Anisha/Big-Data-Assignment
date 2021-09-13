#!/usr/bin/python3
import sys

#!/usr/bin/env python
import sys
state_city=dict()

for line in sys.stdin:
    obj, count = line.split(",")
    city=obj["state"]
    state=obj["city"]

    try:
        count = int(count)
    except ValueError:
        continue

    if state not in state_city.keys():
        state_city[state].append((city,0)) 
    state_city[state] += count
    

for city in sorted(state_city.keys()):
	print("{}\t{}".format(city, state_city[city]))
