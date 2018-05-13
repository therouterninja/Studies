"""In place mergesort."""

def merge(left, right, myarray):
  l, r, m = 0, 0, 0
  while l != len(left) and r != len(right):
    if left[l] < right[r]:
      myarray[m] = left[l]
      l += 1
    else:
      myarray[m] = right[r]
      r += 1
    m += 1

  myarray[m:] = left[l:] + right[r:]
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
