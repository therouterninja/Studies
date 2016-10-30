"""Simple binary tree implementation."""

def _binsearch(myarray, target, start_idx, end_idx):
  midpoint = start_idx + (end_idx - start_idx)/2
  if myarray[midpoint] == target:
    return midpoint
  else:
    if target > myarray[midpoint]:
      if start_idx+1 == midpoint:
        return
      else:
        return _binsearch(myarray, target, midpoint+1, end_idx)
    else:
      if end_idx == 0:
        return
      return _binsearch(myarray, target, start_idx, midpoint)

def binsearch(myarray, target):
  return _binsearch(myarray, target, 0, len(myarray))


# Positive tests
print(binsearch([1,2,5,6,8,25,40,45,47,49,50], 40))
print(binsearch([1,2,5,6,8,25,40,45,47,49,50], 49))

# Negative tests
print(binsearch([1,2,5,6,8,25,40,45,47,49,50], 55))
print(binsearch([1,2,5,6,8,25,40,45,47,49,50], 46))
print(binsearch([1,2,5,6,8,25,40,45,47,49,50], 0))
