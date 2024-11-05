# Time Complexity: O(n)
# Space Complexity: O(1)
# Stack
def validParentheses(s):
  pairs = {
      "(": ")",
      "[": "]",
      "{": "}",
      }

  stack = []

  for ch in s:
    # check is ch opening
    if ch in pairs:
      stack.append(ch)
    else:
      if not stack:
        return False

      top = stack.pop()
      if pairs[top] != ch:
        return False

  return True if not stack else False



print("res:", validParentheses(")()"))

"""

add opening brackets to stack

  add opening brackets to the stack 
    when closing bracket comes the top item of the stack must be the opening of the closing
      otherwise return False


"""
