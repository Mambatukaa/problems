
"""
fib(0) = 0
fib(1) = 1

fib(n) = fib(n - 1) + fib(n - 2)


"""


# Brute force approach
# Time Complexity: O(2^n)
# Space Complexity: O(2^n)
def fibBruteForce(n):
  if n <= 1:
    return n

  return fibBruteForce(n - 1) + fibBruteForce(n - 2)

print(fibBruteForce(12))


# Top to bottom DP
# Recursive with memo (cache)
# Time Complexity: O(n)
# Space Complexity: O(n)

def fibTopToBottom(n, memo):
  if n <= 1:
    return n

  if n in memo:
    return memo[n]
  
  memo[n] = fibTopToBottom(n - 1, memo) + fibTopToBottom(n - 2, memo)
  
  return memo[n]

print(fibTopToBottom(12, {}))

# Bottom to TOP DP
# Iterative solution with an array
# Time Complexity: O(n)
# Space Complexity: O(n)
def fibBottomToTop(n):
  if n <= 1:
    return n

  dp = [0, 1]
  i = 2

  while i <= n:
    temp = dp[1]

    dp[1] = dp[0] + dp[1]
    dp[0] = temp
    i += 1

  return dp[1]

print(fibBottomToTop(12))

# Bottom to TOP DP
# Iterative solution with 2 pointers
# Time Complexity: O(n)
# Space Complexity: O(1)
def fibBottomToTopII(n):
  if n <= 1:
    return n

  p1 = 0
  p2 = 1
  i = 2

  while i <= n:
    temp = p2

    p2 = p1 + p2 
    p1 = temp
    i += 1

  return p2

print(fibBottomToTopII(100))
