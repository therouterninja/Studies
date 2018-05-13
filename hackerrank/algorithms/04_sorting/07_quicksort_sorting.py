#!/bin/python

m = input()
ar = [int(i) for i in raw_input().strip().split()]

def quickSort(ar):
    partition = ar[0]
    bottom_array = []
    middle_array = []    
    top_array = []

    for i,v in enumerate(ar):
        if v > partition:
            top_array.append(v)
        elif v < partition:
            bottom_array.append(v)
        else:
            middle_array.append(v)
    if len(bottom_array) > 1:
        bottom_array = quickSort(bottom_array)
    if len(top_array) > 1:
        top_array = quickSort(top_array)
    print " ".join(map(str, bottom_array + middle_array + top_array))
    return bottom_array + middle_array + top_array

quickSort(ar)
