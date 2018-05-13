def insertion_sort(l):
    for i in xrange(1, len(l)):
        key = l[i]
        while (i > 0) and (l[i-1] > key):
           l[i] = l[i-1]
           i -= 1
            
        l[i] = key
        #print ar

m = input()
ar = [int(i) for i in raw_input().strip().split()]
insertion_sort(ar)
print " ".join(map(str,ar))
