#!/usr/bin/python3
#!/usr/bin/env python
import sys
hourCount = {}


for line in sys.stdin:
    hour, count = line.split(",")
    hour = int(hour.strip())
    count = count.strip()

    try:
        count = int(count)
    except ValueError:
        continue
    
    
    if hour not in hourCount.keys():
        hourCount[hour] = 0
    hourCount[hour]+= count
 
for hour in sorted(hourCount.keys()):
	print("{}\t{}".format(hour, hourCount[hour]))
