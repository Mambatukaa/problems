"""
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
# Time Complexity: 4^n / /n
# Space Complexity: 4^n / n
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        self.res = []


        def backtracking(curr, opening, closing):
            if opening + closing == n * 2:
                self.res.append("".join(curr))
                return

            if opening < n:
                curr.append("(")
                backtracking(curr, opening + 1, closing)
                curr.pop()

            if opening > closing:
                curr.append(")")
                backtracking(curr, opening, closing + 1)
                curr.pop()

        backtracking([], 0, 0)

        return self.res

