""""
You are given a O-indexed 2D integer matrix grid of size n * n with values in the range [1, n2]. Each integer
appears exactly once except a which appears twice and b which is missing. The task is to find the repeating
and missing numbers a and b.
Return a O-indexed integer array ans of size 2 where ans [0] equals to a and ans [1] equals to b.

Example 1:
    Input: grid = [[1,3],[2,2]]
    Output: [2,4]
    Explanation: Number 2 is repeated and number 4 is missing so the answer is 12,41.

Example 2:
    Input: grid = [[9,1,71,[8,9,21,[3,4,611
    Output: [9,5]
    Explanation: Number 9 is repeated and number 5 is missing so the answer is [9,5].








"""
class Solution:
    # Time Complexity: O(n^2)
    # Space Complexity: O(n^2)
    def findMissingAndRepeatedValues(self, grid):
        n = len(grid)
        seen = set()

        currSum = (n*n)*((n*n) +1)//2

        res = [0, 0]
        
        for r in range(n):
            for c in range(n):
                curr = grid[r][c]

                if curr in seen:
                    res[0] = curr
                else:
                    seen.add(curr)
                    currSum -= curr
                    

        res[1] = currSum


        return res





      
        



grid = [[1,3],[2,2]]

solution = Solution()

print("res:", solution.findMissingAndRepeatedValues(grid))
