

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

print(minCost([10, 15, 20]))





"""
cost = [10, 15, 20]
output: 15


min cost to reach len(cost) 3th idx.


curr = min(curr - 1, curr - 2)



"""
