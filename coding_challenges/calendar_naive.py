"""Naive approach at merging two calendars and inverting to find open spaces."""

p1 = [[100, 200], [400,450], [600,700]]
p2 = [[200, 250], [300,400], [500,550], [550,575]]

def merge_calendar(p1, p2):
  # Simple naive approach ( nlogn)
  oldlist = p1+p2
  oldlist.sort()
  newlist = [oldlist[0]]


  for curr_start, curr_end in oldlist[1:]:
    if curr_start > newlist[-1][1]:
      newlist.append([curr_start, curr_end])
    elif curr_start == newlist[-1][1]:
      newlist[-1][1] = curr_end
    elif curr_start < newlist[-1][1]:
      if curr_end > newlist[-1][1]:
        newlist[-1][1] = curr_end
      elif curr_end <= newlist[-1][1]:
        continue
  return newlist

def invert_calendar(calendar_list, start=0, end=1440):
  newlist = []
  start = start

  for idx, val in enumerate(calendar_list):
    if idx == len(calendar_list)-1:
      newlist.append([start, val[0]])
      newlist.append([val[1], end])
    else:
      newlist.append([start, val[0]])
      start = val[1]
  return newlist

results = merge_calendar(p1, p2)
print invert_calendar(results)
