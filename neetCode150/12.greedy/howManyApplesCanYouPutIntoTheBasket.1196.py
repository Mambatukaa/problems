# Time Complexity: O(n log n)
# Space Complexity: O(1)
# Greedy
class Solution:
    def maxNumberOfApples(self, weight):
      weight.sort()

      res = 0
      curr = 0

      for w in weight:
        curr += w

        if curr > 5000:
          return res
        
        res += 1

      return res


solution = Solution()

weight = [5002, 4996, 5000, 4]

print(solution.maxNumberOfApples(weight))
