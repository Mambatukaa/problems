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
houseRobber(nums)

