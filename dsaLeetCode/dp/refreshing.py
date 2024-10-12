"""


  What exactly is DP?

    In short, dynamic programming is just optimized recursion. Let's say you had some recursive function that
    returned the answer to the original problem treating whatever you call the function with as the input. We saw
    this idea extensively in the tree section. For example, we would frequently define a function dfs • that took a
    node and returned the answer to the original problem as if the input was the subtree rooted at node .


"""


# Top to Bottom approach (RECURSIVE)
# Time Complexity: O(n)
# Space COmplexity: O(n)
def fibonacci(n):
  if n < 0:
    return 0

  memo = {0: 0, 1: 1}

  # recursive
  def fib(n):
    if n in memo:
      return memo[n]

    res = fib(n - 1) + fib(n - 2)

    memo[n] = res

    return res

  # iterative
  # Time Complexity: O(n)
  # Space Complexity: O(n)
  def fibII(n):
    if n < 1:
      return 0

    dp = [0] * (n + 1)
    dp[1] = 1

    for i in range(2, n + 1):
      dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]

  
  # iterative II
  # Time Complexity: O(n)
  # Space Complexity: O(1)
  def fibIII(n):
    if n < 1:
      return 0

    #    [n - 1, n]
    dp = [0, 1]

    for i in range(2, n + 1):
      dp[0], dp[1] = dp[1], dp[0] + dp[1]
      
    return dp[1]

  return fibIII(n)


# print("res:", fibonacci(10))


def houseRobber(nums):


  # iterative
  # Time Complexity: O(n)
  # Space Complexity: O(1)
  def rob(nums):
    skipped = 0
    currMax = 0

    for num in nums:
      currMax, skipped = max(currMax, skipped + num), currMax

    return currMax

  # recursive
  # Time Complexity: O(n)
  # Space Complexity: O(n)
  def robII(nums):

    memo = {}

    def helper(idx):
      if idx < 0:
        return 0

      if idx <= 1:
        return nums[idx]

      if idx in memo:
        return memo[idx]

      memo[idx] = nums[idx] + max(helper(idx - 2), helper(idx - 3))
      
      return memo[idx]
    
    return max(helper(len(nums) - 1), helper(len(nums) - 2))


  # Recursive
  # Top Down
  # Time Complexity: O(n)
  # Space Complexity: O(n)
  def robIII(nums):
    memo = {}

    def helper(idx):
      if idx < 0:
        return 0

      if idx == 0:
        return nums[idx]

      if idx in memo:
        return memo[idx]

      withCurrent = nums[idx] + helper(idx - 2)
      skipped = helper(idx - 1)

      memo[idx] = max(withCurrent, skipped)

      return max(withCurrent, skipped)

    return max(helper(len(nums) - 1), helper(len(nums) - 2))

  # Recursive
  # Top Down
  # Time Complexity: O(n)
  # Space Complexity: O(n)
  def robIV(nums):
    memo = {}

    def helper(idx):
      if idx < 0:
        return 0

      if idx <= 1:
        return nums[idx]

      if idx in memo:
        return memo[idx]

      memo[idx] = nums[idx] + max(helper(idx - 2), helper(idx - 3))

      return memo[idx]

    return max(helper(len(nums) - 1), helper(len(nums) - 2))

  print("Res 1:", rob(nums))
  print("Res 2:", robII(nums))
  print("----------------------------")
  print("Res 3:", robIII(nums))
  print("Res 4:", robIV(nums))

nums = [2, 1, 1, 2]
#houseRobber(nums)



# MINIMUM COST CLIMBING STAIRS

def minCostClimbingStairs(cost):

  # FORMULA dp[100] = min(dp[99] + cost[99], dp[98] + cost[98])

  # Top-Down Recursive
  # Time Complexity: O(n)
  # Space Complexity: O(n)
  def minCostIII():
    # Formula = dp(100) = min(dp(99) + cost[99], dp(98) + cost[98])
    memo = [-1] * (len(cost) + 1)

    def helper(idx):
      if idx <= 1:
        return 0

      if memo[idx] != -1:
        return memo[idx]

      memo[idx] = min(helper(idx - 1) + cost[idx - 1], helper(idx - 2) + cost[idx - 2])

      return memo[idx]

    return helper(len(cost))


  # Top-Down Recursive
  # Time Complexity: O(n)
  # Space Complexity: O(n)
  def minCost():
    memo = [-1] * len(cost)

    def helper(idx):
      if idx >= len(cost):
        return 0

      if memo[idx] != -1:
        return memo[idx]
      
      # make two decisions
      memo[idx] = cost[idx] + min(helper(idx + 1), helper(idx + 2))

      return memo[idx]
    
    return min(helper(0), helper(1))

   # add solution using iterative
   # Bottom-UP solution
   # Time Complexity: O(n)
   # Space Complexity: O(1)
  def minCostII():
    step = 0
    jump = 0

    for c in cost:
      step, jump = min(step + c, jump + c), step

    return min(step, jump)


   # add solution using iterative
   # Bottom-UP solution
   # Time Complexity: O(n)
   # Space Complexity: O(n)
  def minCostIV():
    n = len(cost)

    dp = [0] * (n + 1)

    for i in range(2, n + 1):
      dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

    return dp[n]

  print("Res 1:", minCost())
  print("Res 2:", minCostII())
  print("Res 3:", minCostIII())
  print("Res 4:", minCostIV())

cost = [10, 15, 20, 10, 15, 20]

minCostClimbingStairs(cost)

