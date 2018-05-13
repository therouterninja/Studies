"""Better approach at merging two calendars and inverting to find open spaces."""

p1 = [[100, 200], [400,450], [600,700]]
p2 = [[200, 250], [300,400], [500,550], [550,575], [800,900], [900,1000], [1000,1200]]


def merge_calendars(p1, p2):
  newlist = []
  done_ctr = 0
  p1_idx = 0
  p2_idx = 0

  while done_ctr < len(p1+p2)-1:
    # Get the lowest start time of p1 or p2 to start us off
    if p1_idx < len(p1) and p1[p1_idx][0] <= p2[p2_idx][0]:
      curr_ptr = p1[p1_idx]
      p1_idx += 1
    else:
      curr_ptr = p2[p2_idx]
      p2_idx += 1

    # If first entry, just add it.
    if not newlist:
      newlist.append(curr_ptr)
      continue

    # Greater than last end, just add it.
    if curr_ptr[0] > newlist[-1][1]:
      newlist.append(curr_ptr)
    # If current start less than last start.
    elif curr_ptr[0] >= newlist[-1][0]:
      # If current end greater, set last end to this one.
      if curr_ptr[1] > newlist[-1][1]:
        newlist[-1][1] = curr_ptr[1]
      # Otherwise this is contained by last end.  Do nothing.
      elif curr_ptr[1] <= newlist[-1][1]:
        continue

    done_ctr += 1
  return newlist

print(merge_calendars(p1, p2))
