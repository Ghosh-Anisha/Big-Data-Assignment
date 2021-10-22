#!/usr/bin/python3

import sys
import json
import math

f=open(sys.argv[1],"r")
f1=open(sys.argv[2],"r")
pgranks = dict()

for line in f.readlines():
    source, pg = line.strip().split(',')
    pgranks[source] = pg

temp=json.loads(f1.readlines())

for line in sys.stdin:
    #1 [2,3,4]
    source= line.split('\t')[0]
    dest=line.split('\t')[1]
    contribution = pgranks[source]/len(dest)
    similarity= lambda v1, v2 : sum(x*y for x, y in zip(v1, v2)) / (math.sqrt(sum(i*i for i in v1)) * math.sqrt(sum(i*i for i in v2)))
    for i in dest:
        sim=similarity(temp[source],temp[i])
        print(i,source,contribution*sim)

