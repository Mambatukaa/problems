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

  print("Res 1:", rob(nums))

nums = [1, 3, 4, 7, 10]
houseRobber(nums)

