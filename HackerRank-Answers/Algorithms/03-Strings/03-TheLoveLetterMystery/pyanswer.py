# Enter your code here. Read input from STDIN. Print output to STDOUT

for _ in range (input()):
    alist = list(raw_input())
    findex = 0
    bindex = len(alist) - 1
    steps = len(alist)//2
    total = 0
    
    for step in range(steps):
        total += abs(ord(alist[step]) - ord(alist[bindex]))
        
        findex += 1
        bindex -= 1
        
    print total