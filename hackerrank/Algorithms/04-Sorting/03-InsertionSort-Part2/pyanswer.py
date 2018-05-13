#!/bin/python

m = input()
arr = [int(i) for i in raw_input().strip().split()]

def insertionSort(index, value):
    while index > 0 and value < arr[index-1]:
        arr[index] = arr[index-1]
        index -= 1

    arr[index] = value

for i, v in enumerate(arr):
    if i != 0:
        insertionSort(i, v)
        print " ".join(map(str, arr))