#!/usr/bin/env python3

import sys
import json
import datetime
output = dict()

for line in sys.stdin:
	line= line.strip()
	ob=json.loads(line)
	attr_count=0
	if ob['Description'] in ["lane blocked", "shoulder blocked","overturned vehicle" ]:
		attr_count+=1
	if ob['Severity'] >= 2:
		attr_count+=1
	if ob['Sunrise_Sunset'] == 'Night':
		attr_count+=1
	if ob['Visibility(mi)'] <= 10.0:
		attr_count+=1
	if ob['Precipitation(in)'] >=0.2:
		attr_count+=1
	if ob['Weather_Condition'] in ["Heavy Snow", "Thunderstorm", "Heavy Rain", "Heavy Rain Showers", "Blowing Dust"]:
		attr_count+=1

	if attr_count== 6:
		output[hour]. append(1)