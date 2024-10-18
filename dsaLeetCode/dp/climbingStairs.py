

# Time Complexity: O(n)
# Space Complexity: O(1)
# Bottom UP iterative solution
def climbingStairs(n):
  # climbingStairs(n) = climbingStairs(n - 1) + climbingStairs(n - 2)

  if n == 1:
    return 1

  first, second = 1, 2

  for step in range(3, n + 1):
    first, second = second, first + second

  return second


# Time Complexity: O(n)
# Space Complexity: O(n)
# Top down approach recursive
def climbingStairsII(n):
  if n == 1:
    return 1

  def dp(n):
    if n in memo:
      return memo[n]

    if n <= 1:
      return 1

    memo[n] = dp(n - 1) + dp(n - 2)

    return memo[n]

  memo = {}
  dp(n)

  return memo[n]


print("Res 1:", climbingStairs(40))
print("Res 2:", climbingStairsII(40))



"""

You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?




Start to calculate first steps. 

climbingStairs(n) = climbingStairs(n - 1) + climbingStairs(n - 2)

"""
