# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
      # sliding window

      l = 0
      seen = set()
      res = 0

      for r in range(len(s)):
        curr = s[r]

        # shrink until remove duplicates
        while curr in seen:
          seen.remove(s[l])
          l += 1
        
        seen.add(s[r])

        res = max(res, r - l + 1)
      
      return res


solution = Solution()
s = "abcabcbb"

print(solution.lengthOfLongestSubstring(s))
        
