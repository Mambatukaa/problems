# Time Complexity: O(n)
# Space Complexity: O(n)
# STACK PROBLEM DS
def validParenthesis(s):
  pair = {
      "(": ")",
      "[": "]",
      "{": "}"
      }

  stack = []

  for ch in s:
    if ch in pair:
      stack.append(ch)
    else:
      # edge case
      if not stack:
        return False
      
      lastOpening = stack.pop()

      if ch != pair[lastOpening]:
        return False

  return len(stack) == 0

print(validParenthesis("[]()({[]})[}"))

"""
Given a string s containing just the characters '(', ')', '{', '}' '[', ']'. Check the string is valid.

Valid if:
  1. Open brackets must be closed by the same type of brackets.
  2. Open brackets must be closed in the correct order.
  3. Every close bracket has a corresponding open bracket of the same type.



1. The first closing bracket must close the right bracket. If it can't return false else continue.

2. To check the order use Stack data structure.



"""
