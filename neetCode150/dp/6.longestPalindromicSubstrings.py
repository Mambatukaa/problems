# Time Complexity: O(n^2)
# Space Complexity: O(1)
# DP
# Ruse a previously computed palindrome
class Solution:
    def countSubstrings(self, s: str) -> int:

      # check palindromic on every substring

      counter = 0

      for i in range(len(s)):
        l = i
        r = i

        # is in range
        while l >= 0 and r < len(s) and s[l] == s[r]:
          counter += 1

          l -= 1
          r += 1

        l = i
        r = i + 1

        # is in range
        while l >= 0 and r < len(s) and s[l] == s[r]:
          counter += 1

          l -= 1
          r += 1
      
      return counter

solution = Solution()

print(solution.countSubstrings("abc"))
        
