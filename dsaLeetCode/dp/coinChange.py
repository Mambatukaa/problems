# Backtracking solution 
# Time Complexity: O(2^n)
def coinChange(coins, amount):
  coins.sort(reverse=True)


  def backtracking(curr, currSum):
    if currSum == amount:
      return True
      

    if currSum > amount:
      return False


    for coin in coins:
      curr.append(coin)
      res = backtracking(curr, currSum + coin)

      if res:
        return curr

      curr.pop()


  return len(backtracking([], 0))



print("res:", coinChange([1,2,5], 11))
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
