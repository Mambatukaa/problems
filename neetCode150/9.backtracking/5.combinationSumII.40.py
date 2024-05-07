# Time Complexity: O(n * 2^n)
# Space Complexity: O(n * 2^n)
# 10 minutes
class Solution:
    def combinationSum2(self, candidates, target):
      res = []
      candidates.sort()

      def backtracking(curr, currSum, start):
        if currSum > target:
          return
        
        if currSum == target:
          res.append(curr[:])
        
        for i in range(start, len(candidates)):
          if start < i and candidates[i - 1] == candidates[i]:
            continue

          candidate = candidates[i]
          curr.append(candidate)
          backtracking(curr, currSum + candidate, i + 1)
          curr.pop()

      backtracking([], 0, 0)

      return res

solution = Solution()

solution.combinationSum2([10,1,2,7,6,1,5], 8)


# Different solution
# Time Complexity: O(n * 2^n)
# Space Complexity: O(n * 2^n)
# Back tracking

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
      res = []
      candidates.sort()
      curr = []

      def backtracking(target, start):
        if target == 0:
          res.append(curr[:])
        
        for i in range(start, len(candidates)):
          if start < i and candidates[i - 1] == candidates[i]:
            continue
          
          candidate = candidates[i]

          if candidate > target:
            return 

          curr.append(candidate)
          backtracking(target - candidate, i + 1)
          curr.pop()

      backtracking(target, 0)

      return res
