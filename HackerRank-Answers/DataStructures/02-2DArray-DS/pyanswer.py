#!/bin/python

import sys

arr = []
top_value = 0
for arr_i in xrange(6):
    arr_temp = map(int,raw_input().strip().split(' '))
    arr.append(arr_temp)

x = None
for i,row in enumerate(arr):
    for j,cell in enumerate(row):
        try:
            x = max(arr[i][j] + arr[i][j + 1] + arr[i][j + 2] + arr[i + 1][j + 1] + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2], x)
        except:
            pass
        
print x