""""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
"""

# Backtracking
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []


        def backtracking(opening, closing, curr):
            if len(curr) == n * 2:
                res.append("".join(curr))
                return
            
            if opening < n:
                curr.append("(")
                backtracking(opening + 1, closing, curr)
                curr.pop()
            
            if closing < opening:
                curr.append(")")
                backtracking(opening, closing + 1, curr)
                curr.pop()

        backtracking(0, 0, [])

        return res


