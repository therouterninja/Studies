#!/bin/python

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
   a_temp = map(int,raw_input().strip().split(' '))
   a.append(a_temp)

index1 = 0
index2 = n-1

index1_value = None
index2_value = None

for i,row in enumerate(a):
    if index1_value == None:
        index1_value = a[i][index1]
    else:
        index1_value += a[i][index1]

    if index2_value == None:
        index2_value = a[i][index2]
    else:
        index2_value += a[i][index2]

    index1 += 1
    index2 -= 1

print abs(index1_value - index2_value)