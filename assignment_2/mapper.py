#!/usr/bin/env python3

import sys
import json
import requests

lat= float(sys.argv[1].strip())
long= float(sys.argv[2].strip())
D= float(sys.argv[3].strip())

def euclidean_distance(obj):
    x1=float(ob["Start_Lat"])
    x2=float(ob["Start_Lng"])
    d=((x1-lat)**2+(x2-long)**2)**0.5
    if(d<=D):
        return 1
    return 0

for line in sys.stdin: 
    ob=json.loads(line.strip())

    if euclidean_distance(ob):
      url = 'http://20.185.44.219:5000/'

      myobj =  {"latitude": ob["Start_Lat"], "longitude": ob["Start_Lng"] }

      x = requests.post(url, json = myobj)
      data=x.json()
      
      print(data['state'],",",data['city'],",",euclidean_distance(ob))

    else:
      pass
	

