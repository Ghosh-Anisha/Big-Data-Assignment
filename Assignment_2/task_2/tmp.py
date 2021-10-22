#!/usr/bin/python3

import sys
import json
import math

for line in sys.stdin:
    #1 [2,3,4]
    #print(line)
    source= line.split('\t')[0]
    dest=line.split('\t')[1]
    print(dest)

    # dest= line.split('[')[1]
    # source = source.strip()
    # dest = dest.split(']')[0].split(',')
    #print(source," ", dest)

