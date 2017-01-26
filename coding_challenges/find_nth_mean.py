def find_nth_mean(n, filename):
  total_sum = float()
  row_count = int()
  first_col = True

  with open(filename) as f:
    for line in f:
      # Ignore the first row (column descriptions).
      if first_col:
        first_col = False
        continue

      string_buffer = str()
      start_quote = False
      end_quote = False
      col_count = 1

      for c in line:
        # Quote mode
        if start_quote and end_quote and c == ',':
            col_count += 1
            start_quote = False
            end_quote = False

        # Toggle an end quote if we are in quote mode.
        elif start_quote and not end_quote and c == '"':        
          end_quote = True

        # Since we're in quote mode, just add to the string buffer.
        elif start_quote and col_count == 5:
          string_buffer += c

        # Non Quote Mode
        elif not start_quote and not end_quote and c == '"':
          start_quote = True
        elif not start_quote and not end_quote and c == ',':
          col_count += 1

        # Buffer characters in col 5.
        elif not start_quote and col_count == 5:
          string_buffer += c
        # We don't care about non col 5 characters.
        else:
          pass

        # Add to total if we detect we've hit col 6.   Col 5 should be stored at this point.
        if col_count == 6:
          col_count = 1 # Reset col colunt
          try:
            res = float(string_buffer)
            if res is not None:
              total_sum += res
              row_count += 1
            string_buffer = ""

          except:
            string_buffer = ""
            break
  return (total_sum, row_count, total_sum/row_count)

print find_nth_mean(5, "samplecsv.csv")
