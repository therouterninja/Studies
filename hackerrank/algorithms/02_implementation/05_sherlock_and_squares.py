# Enter your code here. Read input from STDIN. Print output to STDOUT

for _ in range(int(input())):
    square_val = 1
    square_cnt = 0
    
    start, end = raw_input().split()

    while square_val**2 < int(start):
        square_val += 1

    while square_val**2 <= int(end):
        square_val += 1
        square_cnt += 1

    print square_cnt