# Time Complexity: O(amount * len(coins))
# Space Complexity: O(amount)
class Solution:
    def coinChange(self, coins, amount: int) -> int:
      if amount == 0:
        return 0

      dp = [amount + 1] * (amount + 1)
      dp[0] = 0

      for a in range(1, amount + 1):
        for c in coins:
          if a >= c:
            dp[a] = min(dp[a], 1 + dp[a - c])

      return dp[amount] if dp[amount] != amount + 1 else -1

        
solution = Solution()
coins = [1, 3, 4, 5]
amount = 7

print("response: ", solution.coinChange(coins, amount))

"""
0: 0
1: 1
2: 2
3: 1
4: 1
5: 1
6: 2
7: 2



"""
