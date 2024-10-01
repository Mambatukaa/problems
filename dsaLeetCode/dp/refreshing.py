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

  def fib(n):
    if n in memo:
      return memo[n]

    res = fib(n - 1) + fib(n - 2)

    memo[n] = res

    return res

  return fib(n)


print("res:", fibonacci(10))
