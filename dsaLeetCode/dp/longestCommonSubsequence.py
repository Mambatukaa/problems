from collections import deque

"""

2D Dynamic programming


"""



# TOP down approach
# Time Complexity: O(n + m) n = text1.length m = text2.length
# Space Complexity: O(n + m)
def longestCommonSubsequence(text1, text2):
  memo = {}

  def dp(i, j):
    if (i,j) in memo:
      return memo[(i,j)]

    if i >= len(text1) or j >= len(text2):
      return 0

    if text1[i] == text2[j]:
      return 1 + dp(i + 1, j + 1)

    memo[(i,j)] = max(dp(i + 1, j), dp(i, j + 1))

    return memo[(i,j)]

  return dp(0, 0)


# Bottom Up solution
# Time Complexity: O(n * m)
# Space Complexity: O(n * m)
def longestCommonSubsequence(text1, text2):
  ROWS = len(text1)
  COLS = len(text2)

  dp = [[0 for _ in range(COLS + 1)] for _ in range(ROWS + 1)]


  for i in range(ROWS - 1, -1, -1):
    for j in range(COLS - 1, -1, -1):

      if text1[i] == text2[j]:
        dp[i][j] = 1 + dp[i + 1][j + 1]
      else:
        dp[i][j] = max(dp[i + 1][j], dp[i][j + 1])

  return dp[0][0]


text1 = "abcde"
text2 = "ace"

print("res:", longestCommonSubsequence(text1, text2))




