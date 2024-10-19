# Time Complexity: O(n)
# Space Complexity: O(n)
# Top-Down solution
def minCostClimbingStairs(cost):

  n = len(cost)

  dp = cost.copy()

  for i in range(2, n):
    dp[i] = min(dp[i - 2], dp[i - 1]) + cost[i]

  return min(dp[n - 1], dp[n - 2])


# Time Complexity: O(n)
# Space Complexity: O(1)
# Top-Down solution
def minCostClimbingStairsII(cost):
  n = len(cost)
  jump, step = 0, 0

  for i in range(n):
    step, jump = min(step, jump) + cost[i], step

  return min(step, jump)

# Time Complexity: O(n)
# Space Complexity: O(n)
# Bottom UP solution recursive
def minCostClimbingStairsIII(cost):
  n = len(cost)
  memo = [-1] * len(cost)

  def dp(idx):
    if idx >= n:
      return 0

    if memo[idx] != -1:
      return memo[idx]

    memo[idx] = min(dp(idx + 1), dp(idx + 2)) + cost[idx]

    return memo[idx]

  return min(dp(0), dp(1)) 

cost = [1,100,1,1,1,100,1,1,100,1]
print("Res:", minCostClimbingStairs(cost))
print("Res II:", minCostClimbingStairsII(cost))
print("Res III:", minCostClimbingStairsIII(cost))

"""
You are given an integer array cost where cost [i] is the cost of ith step on a staircase. 
  Once you pay the cost, you can either climb one or two steps.


You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.


Ex 1:
  cost = [10, 15, 20]
  Output: 15



One or two steps. return possible min cost to reach the top.

dp[1] = min(dp[2], dp[3]) + dp[1]

"""
