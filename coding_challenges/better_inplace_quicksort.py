def inplace_quicksort(array, start_idx=0, end_idx=None):
  # Set end_idx to length by default
  if end_idx == None:
    end_idx = len(array)-1

  # If only one value, we know it's already sorted.
  if end_idx - start_idx < 1:
    return

  pivot_value = array[end_idx]
  wall_idx = start_idx

  for idx, val in enumerate(array[start_idx:end_idx]):
    if val <= pivot_value:
      array[start_idx+idx], array[wall_idx] = array[wall_idx], array[start_idx+idx]
      wall_idx += 1


  # Swap pivot value(end) with wall index if it's smaller.
  if array[wall_idx] > pivot_value:
    array[wall_idx], array[end_idx] = array[end_idx], array[wall_idx]

  inplace_quicksort(array, wall_idx+1, end_idx)
  inplace_quicksort(array, start_idx, wall_idx-1)

myarray = [1,5,2,4,3,1,6,7,1,2,6,10,22,12,15,8,8]
inplace_quicksort(myarray)
print myarray
