#!/bin/python
from __future__ import division
import sys


n = int(raw_input().strip())
arr = map(int,raw_input().strip().split(' '))

total = 0
positive = 0
negative = 0
zero = 0

for num in arr:
    if num == 0:
        zero += 1
    elif num > 0:
        positive += 1
    elif num < 0:
        negative += 1
    else:
        print "wtf"
    total +=1

print positive/total
print negative/total
print zero/total