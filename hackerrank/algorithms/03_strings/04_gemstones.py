# Enter your code here. Read input from STDIN. Print output to STDOUT

list_of_sets = []
for _ in range(input()):
    list_of_sets.append(set([c for c in raw_input()]))

print len(set.intersection(*list_of_sets))