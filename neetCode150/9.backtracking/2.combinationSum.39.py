# Time Complexity: O(2^t)
# Space Complexity: O(2^t)
# Gave up
class Solution:
    def combinationSum(self, candidates, target):
      res = []

      def backtracking(curr, currSum, idx):
        if idx >= len(candidates) or currSum > target:
          return

        if currSum == target:
          res.append(curr.copy())
          return

        
        for i in range(idx, len(candidates)):
          candidate = candidates[i]
          curr.append(candidate)
          backtracking(curr, currSum + candidate, idx)
          curr.pop()
          idx += 1

      backtracking([], 0, 0)
        
      return res

        
solution = Solution()

print(solution.combinationSum([2,3,6,7], 7))

# Neetcode solution 
# Decision tree
# 2 decisions one with current one with next element
class Solution1:
    def combinationSum(self, candidates, target):
      res = []

      def backtracking(curr, currSum, idx):
        if idx >= len(candidates) or currSum > target:
          return

        if currSum == target:
          res.append(curr.copy())
          return

        curr.append(candidates[idx])

        backtracking(curr, currSum + candidates[idx], idx)
        curr.pop()
        backtracking(curr, currSum, idx + 1)

      backtracking([], 0, 0)
        
      return res

solution1 = Solution1()

print(solution1.combinationSum([2,3,6,7], 7))
