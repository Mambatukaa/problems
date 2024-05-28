# Time Complexity: O(n)
# Space Complexity: O(n)
# Greedy
class Solution:
    def maxArea(self, height) -> int:
      l = 0
      r = len(height) - 1

      res = 0

      while l <= r:
        left = height[l]
        right = height[r]

        res = max(res, (r - l) * min(left, right))

        if left < right:
          l += 1
        else:
          r -= 1

      return res



solution = Solution()

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]

print(solution.maxArea(height))


