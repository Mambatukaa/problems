# Time Complexity: O(n^2)
# Space Complexity: O(1)
# DP
# Reuse a previously computed palindrome
class Solution:
    def countPali(self, s, l, r):
      counter = 0

      while l >= 0 and r < len(s) and s[l] == s[r]:
        counter += 1

        l -= 1
        r += 1

      return counter

    def countSubstrings(self, s: str) -> int:

      # check palindromic on every substring
      counter = 0

      for i in range(len(s)):
        counter += self.countPali(s, i, i)
        counter += self.countPali(s, i, i + 1)

      return counter

solution = Solution()

print(solution.countSubstrings("abc"))
        
