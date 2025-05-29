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



fill opening first and fill with closing 


( ( (

) ) )

"""

class Solution:
    # Time Complexity: O(2^n)
    # Space Complexity: O(2^n)
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        stack = []
        def backtracking(left, right):
            if left + right == n * 2:
                res.append("".join(stack))

            if left < n:
                stack.append("(")
                backtracking(left + 1, right)
                stack.pop()

            if left > right:
                stack.append(")")
                backtracking(left, right + 1)
                stack.pop()

        backtracking(0, 0)
        
        return res

solution = Solution()

print("res:", solution.generateParenthesis(3))
