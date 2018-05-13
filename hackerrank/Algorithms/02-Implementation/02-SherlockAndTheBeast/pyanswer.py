#!/bin/python

import sys


for _ in range(int(input())):
    n = int(input())
    c = 5*(-n%3)
    if c > n:
        print(-1)
    else:
        print('5' * (n-c) + '3'*c)