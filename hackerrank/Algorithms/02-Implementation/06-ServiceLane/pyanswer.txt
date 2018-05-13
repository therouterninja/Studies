#!/bin/python

import sys


n,t = raw_input().strip().split(' ')
n,t = [int(n),int(t)]
width = map(int,raw_input().strip().split(' '))
for a0 in xrange(t):
    i,j = raw_input().strip().split(' ')
    i,j = [int(i),int(j)]

    low_common_value = None
    for value in width[i:j+1]:
      if not low_common_value:
          low_common_value = value

      if low_common_value > value:
          low_common_value = value
    print low_common_value