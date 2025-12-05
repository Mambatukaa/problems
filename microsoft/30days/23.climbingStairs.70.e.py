""""
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
"""



class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        # one step or 2 steps

        first = 1
        second = 2

        for i in range(2, n):
            third = first + second
            first = second
            second = third

        return second
            



        
class Solution:
    def climbStairs(self, n: int) -> int:

        def rec(i):
            if i > n:
                return 0
            
            if i == n:
                return 1
            
            return rec(i + 1) + rec(i + 2)

        return rec(0)
        
# DP TOP DOWN

class Solution:
    def climbStairs(self, n: int) -> int:

        memo = {}

        def rec(i):
            if i > n:
                return 0
            
            if i == n:
                return 1
            
            if i in memo:
                return memo[i]
            
            memo[i] = rec(i + 1) + rec(i + 2)


            return memo[i]
        return rec(0)


# DP Bottom up
class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        dp = [0] * n

        dp[0] = 1
        dp[1] = 2

        for i in range(2, n):
            dp[i] = dp[i - 2] + dp[i - 1]
        
        return dp[-1]


