

# Brute force BACKTRACKING
# Leetcode solution
# Time Complexity: O(n^s)
# Space Complexity: O(n)
# Time LIMIT EXCEEDED
def coinChange(coins, amount):
  def dfs(remain):
    if remain < 0:
      return -1
    if remain == 0:
      return 0

    minCount = float('inf')
    for coin in coins:
      count = dfs(remain - coin)

      # wrong path
      if count == -1:
        continue
      
      minCount = min(minCount, count + 1)
    
    return -1 if minCount == float('inf') else minCount

  return dfs(amount)

# Backtracking solution 
# Top Down
# Memo
# Time Complexity: O(n * S)
# Space Complexity: O(S)
def coinChangeII(coins, amount):
  def dfs(remain):
    if remain in memo:
      return memo[remain]

    if remain < 0:
      return -1
    if remain == 0:
      return 0

    minCount = float('inf')
    for coin in coins:
      count = dfs(remain - coin)

      # wrong path
      if count == -1:
        continue
      
      minCount = min(minCount, count + 1)
    
    memo[remain] = -1 if minCount == float('inf') else minCount

    return memo[remain]

  memo = {}
  return dfs(amount)

print("res 1:", coinChange([1, 2, 5], 11))
print("res 2:", coinChangeII([1, 2, 5], 11))

# Dynamic programming
# Bottom UP neetcode
def coinChangeIII(coins, amount):
  dp = [amount + 1] * (amount + 1)
  dp[0] = 0

  for a in range(1, amount + 1):
    for coin in coins:
      if a - coin >= 0:
        dp[a] = min(dp[a], 1 + dp[a - coin])


  if dp[amount] == amount + 1:
    return -1

  return dp[amount]

# Bottom UP solution iterative
def coinChangeIV(coins, amount):
  dp = [float('inf')] * (amount + 1)
  dp[0] = 0

  for coin in coins:
    for a in range(coin, amount + 1):
      dp[a] = min(dp[a], dp[a - coin] + 1)

  return dp[amount] if dp[amount] != float('inf') else -1


# coin = 4, a = 7, dp[7] = min(dp[7], 1 + dp[7-4])

print("res:", coinChangeIV([1, 2, 5], 11))
"""

You are given an integer array coins representing coins of different denominations and an integer amount representing a total
amount of money.

Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any
combination of the coins, return -1.

You may assume that you have an infinite number of each kind of coin.




**********************************************************************

1. Backtracking
  Sort the array by reverse order
  Check every possible combination starts from max element

  if curr == amount:
    return curr.length

  if curr > amount:
    return and try with next small element




"""
