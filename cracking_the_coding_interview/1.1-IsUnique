"""1.1: Is Unique: Implement an algorithm to determine if a string has all unique characters.  What if you cannot use additional data structures?
"""

# Solution 1: dict()
def isunique(mystring):
  mydict = {}
  for letter in mystring:
    if not mydict.get(letter):
      mydict[letter] = True
    else:
      return False
  return True


print(isunique("abcd"))
print(isunique("aabc"))
print(isunique("abca"))

# Solution 2: No data structures
def isunique2(mystring):
  mylist = [False] * 127
  for letter in mystring:
    if mylist[ord(letter)]:
      return False
    mylist[ord(letter)] = True  
  return True

print(isunique2("abcd"))
print(isunique2("aabc"))
print(isunique2("abca"))

# Solution 3: sets()
def isunique3(mystring):
  return len(set(mystring)) == len(mystring)


print(isunique3("abcd"))
print(isunique3("aabc"))
print(isunique3("abca"))

# Solution 4: 
def isunique4(mystring):
  checker = 0
  for c in mystring:
    val = ord(c) - ord('a')
    if (checker & (1 << val) > 0):
      return False
    else:
      checker |= (1 << val)
  return True

print(isunique4("abcd"))
print(isunique4("aabc"))
print(isunique4("abca"))
