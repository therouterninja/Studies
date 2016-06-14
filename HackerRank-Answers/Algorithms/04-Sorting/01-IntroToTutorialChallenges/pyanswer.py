# Enter your code here. Read input from STDIN. Print output to STDOUT

searchvalue = raw_input()
num_values = raw_input()

for i,char in enumerate(raw_input().split()):
    if char == searchvalue:
        print i