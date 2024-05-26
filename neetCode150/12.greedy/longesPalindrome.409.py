from collections import Counter

# Time Complexity: O(n)
# Space Complexity: O(n)
# Greedy
class Solution:
    def longestPalindrome(self, s: str) -> int:
      ctr = Counter(s)
      freqs = ctr.values()

      res = 0

      isOdd = False

      for freq in freqs:
        res += freq // 2 * 2

        if freq % 2 == 1:
          isOdd = True
      
      return res + 1 if isOdd else res

solution = Solution()

s = "abccccdd"

print(2 // 2)
print(5 // 2)
print(6 // 2)
print(8 // 2)

print("s:", solution.longestPalindrome(s))
        

"""
   count characters
   if count is even add to the res
   else trunk to even
"""
