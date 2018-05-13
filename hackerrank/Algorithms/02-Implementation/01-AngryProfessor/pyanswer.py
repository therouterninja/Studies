#!/bin/python

import sys


t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    a = map(int,raw_input().strip().split(' '))

    students_on_time = 0

    for student in a:
        if student <= 0:
            students_on_time += 1
    if students_on_time >= k:
        print "NO"
    else:
        print "YES"