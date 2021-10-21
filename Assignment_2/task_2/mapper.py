#!/usr/bin/python3

import sys
f=open(sys.argv[1],"r")
f1=open(sys.argv[2],"r")
pgranks = dict()

for line in f.readlines():
    source, pg = line.strip().split(',')
    pgranks[source] = pg

for line in sys.stdin:
    #1 [2,3,4]
    source, dest = line.split('[')
    source = source.strip()
    dest = dest.split(']')[0].split(',')
    contribution = pgranks[source]/len(dest)
    for i in dest:
        print(i,contribution)

