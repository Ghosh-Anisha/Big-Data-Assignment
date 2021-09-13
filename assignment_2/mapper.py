#!/usr/bin/python3
import sys
import json
import requests
from datetime import *

lat,long,D=float(sys.argv[1].strip()), float(sys.argv[2].strip()), float(sys.argv[3].strip())

def euclidean_distance(obj):
    x1=float(ob["Start_Lat"])
    x2=float(ob["Start_Lng"])
    d=(x1**2+x2**2)**0.5
    if(d<=D):
        return 1
    return 0


for line in sys.stdin: 
    ob=json.loads(line.strip())


    url = 'http://20.185.44.219:5000/'
    myobj =  {'latitude':float(ob["Start_Lat"]), 'longitude': float(ob["Start_Lng"])}

    x = requests.post(url, data = myobj)
    if euclidean_distance(ob):
        print(x,",",euclidean_distance(ob))
    else:
        pass
	
