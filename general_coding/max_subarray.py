def max_subarray(A):
    max_ending_here = max_so_far = 0
    for x in A:
        max_ending_here = max(0, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
        print x, max_ending_here, max_so_far

    return max_so_far

print(max_subarray([1,2,3,-3,6,-2,-7,10]))
