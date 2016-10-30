def kp(total_cap, items):
  mymatrix = [[0 for i in xrange(total_cap+1)] for j in xrange(len(items))]

  for idx, (weight, value) in enumerate(items):
    for cap in xrange(0 , total_cap+1):
      if weight <= cap:
        mymatrix[idx][cap] = max(mymatrix[idx-1][cap],
                                 (value + mymatrix[idx-1][cap-weight]))
      else:
        mymatrix[idx][cap] = mymatrix[max(idx-1, 0)][cap]
  return mymatrix

total_cap = 7
items = [(1,1), (3,4), (4,5), (7,7)]

print(kp(total_cap, items))
