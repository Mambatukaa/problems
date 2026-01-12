""""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""

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


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        candidates.sort()

        def dfs(i, curr, currSum):
            if currSum == target:
                res.append(curr.copy())
                

            if currSum > target or i == len(candidates):
                return
            print(i, len(candidates))

            curr.append(candidates[i])
            dfs(i + 1, curr, currSum + candidates[i])
            curr.pop()

            while i < len(candidates) and candidates[i - 1] != candidates[i]:
                i += 1
            dfs(i + 1, curr, currSum)
        
        dfs(0, [], 0)
        return res
        
"""

 0 1 2 3 4 5 6
[1,1,2,5,6,7,10]

0


"""
