"""1.5 One Away: There are three types of edits that can be performed on strings:insert a character, remove a character, or replace a character.  Given two strings, write a function to check if they are one edit (or zero edits) away.
"""

def oneaway(string1, string2):
  if len(string1) == len(string2):
    return oneedit(string1, string2)
  elif len(string1) +1 == len(string2):
    return oneinsert(string1, string2)
  elif len(string2) +1 == len(string1):
    return oneinsert(string2, string1)
  return False
    

def oneedit(string1, string2):
  edited = False
  for c1, c2 in zip(string1, string2):
    if c1 != c2:
      if edited:
        return False
      edited = True
  return True

def oneinsert(string1, string2):
  edited = False
  cnt1, cnt2 = 0, 0

  while cnt1 < len(string1) and cnt2 < len(string2):
    if string1[cnt1] != string2[cnt2]:
      if edited:
        return False
      edited = True
      cnt += 1
    else:
      cnt1 += 1
      cnt2 += 1
  return True

print(oneaway("abc", "abd"))
print(oneaway("abc", "abc"))
print(oneaway("abc", "abcd"))
print(oneaway("abcd", "abc"))

print(oneaway("abcd", "ab"))
print(oneaway("ab", "abcd"))
print(oneaway("abcd", "abde"))
print(oneaway("a", "abc"))
