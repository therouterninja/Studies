#!/bin/python

m = input()
ar = [int(i) for i in raw_input().strip().split()]

def quicksort(ar):
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

    return " ".join(map(str, bottom_array + middle_array + top_array))

print quicksort(ar)