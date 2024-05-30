# Time Complexity: O(m * n^m) m = nums.length
# Space Complexity: O(m * n^m) m = nums.length
# Gave up
class SolutionI:
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
        


# NeetCode solution
class Solution:
    def permute(self, nums):
        res = []
        if(len(nums)==1):
            return [nums[:]]

        for i in range (len(nums)):
            print("Nums:", nums)
            n = nums.pop(0)
            perm = self.permute(nums)

            print(perm, 'hahaha')

            for p in perm:
                p.append(n)
            res.extend(perm)
            nums.append(n)

        return res

solution = Solution()

solution.permute([1,2,3])
