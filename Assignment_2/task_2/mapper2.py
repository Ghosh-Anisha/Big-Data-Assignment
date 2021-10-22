#!/usr/bin/python3
import sys
import json
import math

f = open(sys.argv[1], "r")
f1 = open(sys.argv[2], "r")
pgranks = dict()

for line in f.readlines():
    source, pg = line.strip().split(',')
    source = source.strip()
    pg = pg.strip()
    pgranks[int(source)] = int(pg)

temp = json.load(f1)

for line in sys.stdin:
    source, dest = line.split('\t')
    source = source.strip()
    dest = dest.strip()
    dest = dest[1:-1]
    dest = dest.split(',')
    print(source,0,sep=',')

    try:
        contribution = pgranks[int(source)] / len(dest)
    except:
        continue

    def similarity(v1, v2): return sum(x * y for x, y in zip(v1, v2)) / \
        (math.sqrt(sum(i * i for i in v1)) * math.sqrt(sum(i * i for i in v2)))
    for i in dest:
        try:
            sim = similarity(temp[source], temp[i.strip()])
        except:
            continue
        print(i, contribution * sim, sep=',')
f1.close()
f.close()
