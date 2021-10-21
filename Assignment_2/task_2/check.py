#!bin/python3

import sys
import math

file1 = sys.argv[1]
file2 = sys.argv[2]


f1 = open(file1, 'r')
f2 = open(file2, 'r')

dict1 = dict()
# dict2 = dict()

line1 = f1.readlines()
line2 = f2.readlines()

for line in line1:
    s = line.split(',')
    s[1] = s[1][:-1]
    dict1[int(s[0])] = float(s[1])


count = 0
for line in line2:
    s = line.split(',')
    s[1] = s[1][:-1]
    if (abs(dict1[int(s[0])] - float(s[1])) > 0.05):
        print('-'*30)
        print(f"{file1}: {int(s[0])}, {dict1[int(s[0])]}\n{file2}: {int(s[0])}, {float(s[1])}")
        print('-'*30)
        count += 1

print(f"Number of lines different: {count}")

f1.close()
f2.close()

