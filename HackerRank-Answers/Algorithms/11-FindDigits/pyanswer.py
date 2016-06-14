#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n = int(raw_input().strip())

    count=0
    for char in str(n):
        try:
            if int(n)%int(char) == 0:
                count += 1
        except:
            pass
    print count