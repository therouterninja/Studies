#!/bin/python

m = input()
arr = [int(i) for i in raw_input().strip().split()]


def insertionSort(arr):
    number_to_sort = arr[-1]
    current_index = -1

    while current_index > len(arr)*-1 and number_to_sort < arr[current_index-1]:
        arr[current_index] = arr[current_index-1]
        current_index -= 1

        print " ".join(map(str, arr))

        arr[current_index] = number_to_sort
    print " ".join(map(str, arr))

insertionSort(arr)