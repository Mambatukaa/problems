"""
How many different options to reach the top of the mountain taking 1 or 2 steps.


n = 3

1 1 1
2 1
1 2

Output = 3


It looks like decision Tree. 


"""




# Brute force
# Time Complexity: O(2^n)
# Space Complexity: O(2^n)
def climbingStairs(n, totalSteps):
  if n < totalSteps:
    return 0

  if n == totalSteps:
    return 1

  return climbingStairs(n, totalSteps + 1) + climbingStairs(n, totalSteps + 2)



# Dynamic programming
# Top to Bottom
# Time Complexity: O(n)
# Space Complexity: O(n)
def climbingStairsII(n, totalSteps, memo):
  if n < totalSteps:
    return 0

  if n == totalSteps:
    return 1

  if totalSteps in memo:
    return memo[totalSteps]

  memo[totalSteps] = climbingStairsII(n, totalSteps + 1, memo) + climbingStairsII(n, totalSteps + 2, memo)

  return memo[totalSteps]

print(climbingStairsII(100, 0, {}))

# Dynamic programming
# Bottom to Top
# Time Complexity: O(n)
# Space Complexity: O(n)
def climbingStairsBottomToTop(n):
  dp = [1, 2]
  i = 3

  while i <= n:
    temp = dp[1]
    dp[1] = dp[0] + dp[1]
    dp[0] = temp

    i += 1

  return dp[1]


print(climbingStairsBottomToTop(100))

# Dynamic programming
# Bottom to Top
# Time Complexity: O(n)
# Space Complexity: O(1)
def climbingStairsBottomToTopII(n):
  p1 = 1
  p2 = 2
  i = 3

  while i <= n:
    temp = p2
    p2 = p1 + p2
    p1 = temp

    i += 1

  return p2

print(climbingStairsBottomToTopII(100))

# FROM BACK TO FRONT
# Dynamic programming
# Bottom to Top
# Time Complexity: O(n)
# Space Complexity: O(1)
def climbingStairsBottomToTopIII(n):
  one = 1
  two = 1
  
  for i in range(n - 1):
    temp = two
    two = one + two
    one = temp

  return two

print(climbingStairsBottomToTopII(100))
print(climbingStairsBottomToTopIII(100))
