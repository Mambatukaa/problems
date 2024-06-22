# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution:
    def myAtoi(self, s: str) -> int:

      s = s.strip()

      if not s:
        return 0


      sign = -1 if s[0] == "-" else 1

      idx = 1 if s[0] in ["+", "-"] else 0

      res = 0

      for i in range(idx, len(s)):
        ch = s[i]

        if ch not in "0123456789":
          break

        res *= 10
        res += int(ch)

      return max(-2**31, min(sign * res, 2**31-1))

      """
      1. Check edge cases


      """





"""


Input: s = " -042"
Output: -42


Input: s = "0-1"
Output: 0

"""

solution = Solution()

print(solution.myAtoi("-91283472332"))
