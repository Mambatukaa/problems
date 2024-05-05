# Time Complexity: O(n * 2^n)
# Space Complexity: O(n * 2^n)
# Gave up
class Solution:
    def subsets(self, nums):

      res = []
        
      def backtracking(curr, idx):
        if idx > len(nums):
          return

        res.append(curr.copy())

        for i in range(idx, len(nums)):
            curr.append(nums[i])
            print(nums[i], "-------", curr)
            backtracking(curr, i + 1)
            print("*******", curr)
            curr.pop()


        
      backtracking([], 0)
      
      return res

solution = Solution()

print(solution.subsets([1,2,3]))


class SolutionI:
    def subsets(self, nums):
        res = []

        subset = []

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return
            # decision to include nums[i]
            subset.append(nums[i])
            dfs(i + 1)
            # decision NOT to include nums[i]
            subset.pop()
            dfs(i + 1)

        dfs(0)
        return res
