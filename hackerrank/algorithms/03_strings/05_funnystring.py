# Enter your code here. Read input from STDIN. Print output to STDOUT

for _ in range(input()):
    s = raw_input()
    rs = s[::-1]
    n = len(s)
    for i in range(1, n):
        d1 = abs(ord(s[i]) - ord(s[i - 1]))
        d2 = abs(ord(rs[i]) - ord(rs[i - 1]))
        if d1 != d2:
            print("Not Funny")
            break
    else:
        print("Funny")