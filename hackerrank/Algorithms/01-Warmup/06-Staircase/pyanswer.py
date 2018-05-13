#!/bin/python

import sys


n = int(raw_input().strip())

level = 0
staircase = None
staircase_spaces = n-1

while level < n:
    if staircase == None:
        staircase = "#"
    else:
        staircase += "#"
    level +=1
    print " "*staircase_spaces + staircase
    staircase_spaces -= 1