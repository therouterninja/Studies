"""Binary tree approach to finding minimum bad version."""

def FindFailure(version_list, start_idx, end_idx):
  if end_idx - start_idx <= 1:
    return((version_list[start_idx:end_idx+1]))
  else:
    midpoint = start_idx + (end_idx - start_idx) / 2
    state = version_list[midpoint][1]
    if state == "GOOD":
      # Keep looking to the right to find the failure.
      return FindFailure(version_list, midpoint, end_idx)
    else:
      # We're past our failure, go back left.
      return FindFailure(version_list, start_idx, midpoint)
