# Greedy  
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
   def canJump(self, nums):
     goal = len(nums) - 1

     for i in range(len(nums) - 1, -1, -1):
       if i + nums[i] >= goal:
         goal = i

     return True if goal == 0 else False

solution = Solution()
# len = 5
#                       0  1  2  3  4    
print(solution.canJump([1, 2, 0, 1, 0]))
