# Enter your code here. Read input from STDIN. Print output to STDOUT
def insertion_sort(l):
    steps = 0
    for i in xrange(1, len(l)):
        key = l[i]
        while (i > 0) and (l[i-1] > key):
            steps += 1
            l[i] = l[i-1]
            i -= 1
            
        l[i] = key
    return steps

m = input()
ar = [int(i) for i in raw_input().strip().split()]
print insertion_sort(ar)
