# Time Complexity: O(2^n)
# Space Complexity: O(2^n)
def generateParenthesis(n):
  stack = []
  res = []

  def backtrack(openN, closedN):
    if openN == closedN == n:
      res.append("".join(stack))
      return

    if openN < n:
      stack.append("(")
      backtrack(openN + 1, closedN)
      stack.pop()

    if closedN < openN:
      stack.append(")")
      backtrack(openN, closedN + 1)
      stack.pop()

  backtrack(0, 0)

  return res

print("res:", generateParenthesis(3))

"""

Given n pairs of parentheses, write a function to generate all combinations.


Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]



Constraints:
  1 <= n <= 8



opening = 0
closing = 0


1. ( ( ( ) ) )


if opening 

while opening == n:
  p = curr.pop()

  if p == (:
    opening -= 1
  else:
    closing -= 1


2. ( ( ( ) ) )

"""
