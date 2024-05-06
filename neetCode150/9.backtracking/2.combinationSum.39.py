class Solution:
    def combinationSum(self, candidates, target):
      res = []

      def backtracking(curr, currSum):
        if currSum > target:
          return

        if currSum == target:
          res.append(curr.copy())
        
        for i in range(len(candidates)):
          candidate = candidates[i]
          curr.append(candidate)
          backtracking(curr, currSum + candidate)
          curr.pop()
        print('---------', curr)

      backtracking([], 0)
        
      return res

        
solution = Solution()

print(solution.combinationSum([2,3,6,7], 7))
