"""1.4 Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome.  A palindrome is a word or phrase that is the same forwards and backwards.   A permutation is a rearrangement of letters.   The palindrome does not need to be limited to just dictionary words.
"""

# Implement a stack.
def IsPalindrome(mystring):
  mystack = []
  pivot_idx=len(mystring)/2
  for idx, letter in enumerate(mystring):
    if idx < pivot_idx:
      mystack.append(letter)
    elif idx == pivot_idx and len(mystring)% 2 != 0:
      break
    else:
      if letter != mystack.pop():
        return False
  return True

print(IsPalindrome("abccba"))
print(IsPalindrome("abcdcba"))
print(IsPalindrome("abcdadcba"))
print(IsPalindrome("aaaaaaaaaaa"))
