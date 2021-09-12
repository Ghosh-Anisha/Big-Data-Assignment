#!/usr/bin/python3
import sys
import json
from datetime import *

def checkattr(ob):
	attr_count=0
	if "lane blocked" in ob["Description"] or "shoulder blocked" in ob["Description"] or "overturned vehicle" in ob["Description"]:
		attr_count = attr_count + 1
	if ob['Severity'] >= 2:
		attr_count = attr_count + 1
	if ob['Sunrise_Sunset'] == 'Night':
		attr_count = attr_count + 1
	if ob['Visibility(mi)'] <= 10.0:
		attr_count = attr_count + 1
	if ob['Precipitation(in)'] >=0.2:
		attr_count = attr_count + 1
	#if ob['Weather_Condition'] in ["Heavy Snow", "Thunderstorm", "Heavy Rain", "Heavy Rain Showers", "Blowing Dust"]:
	if  "Heavy Snow" == ob['Weather_Condition'] or  "Thunderstorm" == ob['Weather_Condition'] or "Heavy Rain" == ob['Weather_Condition'] or "Heavy Rain Showers" == ob['Weather_Condition'] or "Blowing Dust" == ob['Weather_Condition']:
		attr_count = attr_count + 1
	if attr_count==6:
	   return 1
	return 0


for line in sys.stdin: 
	ob=json.loads(line.strip())
	dt= ob["Start_Time"].split()
	dt= dt[1].split(":")[0]
	hour= int(dt)
	if checkattr(ob):
		print(hour,",",checkattr(ob))
	else:
		pass
	

