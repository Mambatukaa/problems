# Add the subproblems result to the current idx
# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    # sub problems
    def numDecodings(self, s: str) -> int:
      dp = { len(s) : 1 }

      def dfs(i):
        if i in dp:
          return dp[i]
        if s[i] == "0":
          return 0

        res = dfs(i + 1)

        # if it's true we can create pair of 2 digits
        if (i < len(s) - 1 and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456")):
          res += dfs(i + 2)

        dp[i] = res

        return res

      return dfs (0)

    def numDecodingsII(self, s: str) -> int:
      dp = { len(s): 1 }

      for i in range(len(s) - 1, -1, -1):
        if s[i] == "0":
          dp[i] = 0

          continue

        dp[i] = dp[i + 1]

        if (i < len(s) - 1 and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456")):
          dp[i] += dp[i + 2]

      return dp[0]


        
solution = Solution()
s = "112131"
print("res:", solution.numDecodingsII(s))

"""
BBF - 2 2 6
BZ - 2 26
VF - 22 6






"""



