#!/usr/bin/python3

with open('dataset-sample.txt') as f:
    lines = f.readlines()
	
for line in lines:
    temp = line.split()
    print(temp[0],",",temp[1])

