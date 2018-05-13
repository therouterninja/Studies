# Enter your code here. Read input from STDIN. Print output to STDOUT

mystring = raw_input()

all_values = set()
total = 0

for char in mystring:
    all_values.add(char.lower())
 
for value in all_values:
    total += ord(value)

if total == 2879:
    print "pangram"
else:
    print "not pangram"