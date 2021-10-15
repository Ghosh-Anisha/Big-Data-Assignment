#!/usr/bin/python3
import sys

with open('dataset_1percent.txt') as f:
    lines = f.readlines()
	
for line in lines:
    temp = line.split()
    print(temp[0],",",temp[1])

