# Time Complexity: O(m * n^m) m = nums.length
# Space Complexity: O(m * n^m) m = nums.length
# Gave up
class Solution:
    def permute(self, nums):

      res = []


      def backtracking(curr):
        if len(curr) == len(nums):
          res.append(curr.copy())

          return
        
        for i in range(len(nums)):
          if nums[i] in curr:
              continue
          curr.append(nums[i])
          backtracking(curr)
          curr.pop()

      backtracking([])

      return res
        

solution = Solution()

solution.permute([1,2,3])
