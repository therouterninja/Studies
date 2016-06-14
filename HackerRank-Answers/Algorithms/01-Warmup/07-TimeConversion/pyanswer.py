#!/bin/python

import sys


time = raw_input().strip()

time_suffix = time[-2:]
time_tuple = time[:-2].split(":")
time_prefix = int(time_tuple[0]) 

if (time_suffix == "AM" and time_prefix == 12):
    time_tuple[0] = "00"

if (time_suffix == "PM" and time_prefix != 12):          
    time_prefix += 12
    time_tuple[0] = str(time_prefix)

print ":".join(time_tuple)