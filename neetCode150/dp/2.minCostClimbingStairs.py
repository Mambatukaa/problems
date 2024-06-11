# Top to Bottom solution
# Recursive
# Memo
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
  def minCostClimbing(self, cost):
    self.dp = {}

    def helper(cost, n):
      if n <= 1:
        return cost[n]

      if n in self.dp:
        return self.dp[n]
      
      self.dp[n] = cost[n] + min(helper(cost, n - 1), helper(cost, n - 2))

      return self.dp[n]


    n = len(cost)

    return min(helper(cost, n - 1), helper(cost, n - 2))

solution = Solution()

print(solution.minCostClimbing([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))

# Time Complexity: O(n)
# Space Complexity: O(1)
# Bottom To TOP
# 
def minCost(cost):
  dp = [0] * (len(cost) + 1)
  dp[0] = cost[0]
  dp[1] = cost[1]

  cost.append(0)

  for i in range(2, len(dp)):
    dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])

  return dp[-1]

# Time Complexity: O(n)
# Space Complexity: O(1)
# Bottom To TOP
# 
def minCostII(cost):
  cost.append(0)

  for i in range(len(cost) - 3, -1, -1):
    cost[i] = cost[i] + min(cost[i + 1], cost[i + 2])

  return min(cost[0], cost[1])







"""
cost = [10, 15, 20]
output: 15


min cost to reach len(cost) 3th idx.


curr = min(curr - 1, curr - 2)



"""
