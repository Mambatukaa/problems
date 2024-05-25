# Greedy
# Time Complexity: O(n log n)
# Space Complexity: O(1)
class Solution:
    def maxIceCream(self, costs, coins):
      costs.sort()
      res = 0

      for cost in costs:
        coins -= cost

        if coins < 0:
          return res

        res += 1



      return res




solution = Solution()

costs = [7]
coins = 7

print(solution.maxIceCream(costs, coins))
