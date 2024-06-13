

# DP
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Start from the center and expand it
class Solution:
    def longestPalindrome(self, s: str) -> str:
      resL = 0 
      resR = 0
      resLength = 0

      
      for i in range(len(s)):
        left = i
        right = i

        while left >= 0 and right < len(s) and s[left] == s[right]:
          if right - left + 1 > resLength:
            resLength = right - left + 1
            resL = left
            resR = right

          left -= 1
          right += 1
      
        # even length
        left = i
        right = i + 1

        while left >= 0 and right < len(s):
          if s[left] != s[right]:
            break

          if right - left + 1 > resLength:
            resLength = right - left + 1
            resL = left
            resR = right

          left -= 1
          right += 1
        
      return s[resL:resR + 1]


solution = Solution()

print(solution.longestPalindrome("abbbaaac"))
        
