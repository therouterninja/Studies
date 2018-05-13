# Enter your code here. Read input from STDIN. Print output to STDOUT

for _ in range(input()):
    last_char = None
    total_count = 0
    
    for char in raw_input():
        if last_char and last_char == char:
            total_count += 1
        else:
            last_char = char
    print total_count