# Greedy
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def jump(self, nums) -> int:
      res = 0
      start = end = 0

      while end < len(nums) - 1: 
        farthest = 0

        for i in range(start, end + 1):
          farthest = max(farthest, i + nums[i])

        print(start, end, farthest)

        start = end + 1
        end = farthest
        res += 1

      return res

solution = Solution()

print("res:", solution.jump([0]))

