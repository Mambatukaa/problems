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

# NeetCode solution
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        if(len(nums)==1):
            return [nums[:]]

        for i in range (len(nums)):
            n = nums.pop(0)
            perm = self.permute(nums)

            for p in perm:
                p.append(n)
            res.extend(perm)
            nums.append(n)

        return res
