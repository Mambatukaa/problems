# Greedy - Do the right step from the starting point once step failed return FALSE
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
   def canJump(self, nums):
       currIdx = 0
       n = len(nums) - 1
       
       while currIdx < n:
           if nums[currIdx] == 0:
               return False
       
           # update currIdx
           currIdx += nums[currIdx]
           print(currIdx, '========')
        
       return True


solution = Solution()

print(solution.canJump([1,2,0,1,0]))
