"""In place mergesort."""

def merge(left, right, myarray):
  for i in range(len(left + right)):
    if not right or left and left[0] < right[0]:
      myarray[i] = left.pop(0)
    else:
      myarray[i] = right.pop(0)
  return myarray

def mergeSort(myarray):
  if len(myarray) < 2:
    return myarray
  else:
    mid_idx = len(myarray) / 2
    left = mergeSort(myarray[:mid_idx])
    right = mergeSort(myarray[mid_idx:])
    mergearray = merge(left, right, myarray)
    return mergearray

print mergeSort([1,5,4,2,7,9,10,13,3,5])
