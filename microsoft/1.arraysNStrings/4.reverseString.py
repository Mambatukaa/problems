class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def reverseString(self, s):
      l = 0
      r = len(s) - 1

      while l < r:
        s[l], s[r] = s[r], s[l]

        l += 1
        r -= 1



solution = Solution()

s = ["h","e","l","l","o"]
s = ["H","a","n","n","a","h"]

solution.reverseString(s)
        
print(s)
