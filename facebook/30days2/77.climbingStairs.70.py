"""
70. Climbing Stairs
Solved
Easy
Topics
premium lock icon
Companies
Hint
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
        one = 1
        two = 1

        for i in range(n - 1):
            temp = two
            two += one
            one = temp

        return two


"""

  
  s 1 2 3 4 5  6 7
  1 1 2 3 5 8 13
           o t


"""
class Solution:
    def climbStairs(self, n: int) -> int:
        # prev + 1
        # prev.prev + 2
        memo = {}

        def backtracking(i):
            if i in memo:
                return memo[i]
            if i > n:
                return 0
            if i == n:
                return 1

            memo[i] = backtracking(i + 1) + backtracking(i + 2)
            return memo[i]
        return backtracking(0)



            


        


"""
take one step or two step
   


"""
