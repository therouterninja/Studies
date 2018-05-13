def qs(myarray):
  less = list()
  equal = list()
  greater = list()

  if len(myarray) > 1:
    pivot = myarray[0]
    for i in myarray:
      if i > pivot:
        greater.append(i)
      elif i < pivot:
        less.append(i)
      else:
        equal.append(i)
    return qs(less) + equal + qs(greater)
  else:
    return myarray

print qs([6,1,4,2,3,4,4,4,12,3,1,56])
