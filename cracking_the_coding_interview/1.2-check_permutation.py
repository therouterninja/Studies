""" 1.2: Check Permutation: Given two strings, write a method to decide if one is a permutation of the other."""
from collections import defaultdict

# Method 1 - Using Datastructures
# Defaultdict()
# A + B + (A+B)/2
def is_perm1(string1, string2):
  mydict = defaultdict(int)
  for letter in string1:
    mydict[letter] += 1
  for letter in string2:
    mydict[letter] -=1
  for v in mydict.values():
    if v != 0:
      return False
  return True

print(is_perm1("abc", "cba"))
print(is_perm1("abc", "cab"))
print(is_perm1("abc", "cabd"))
print(is_perm1("abc", "cad"))

# Method 2 - No Datastructures
# Sort both strings, then compare
# AlogA + BlogB + 1
def is_perm2(string1, string2):
  string1 = list(string1)
  string1.sort()
  string2 = list(string2)
  string2.sort()
  if string1 == string2:
    return True
  return False


print(is_perm2("abc", "cba"))
print(is_perm2("abc", "cab"))
print(is_perm2("abc", "cabd"))
print(is_perm2("abc", "cad"))
