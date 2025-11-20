""""

Given a string s, return the longest palindromic substring in s.

 

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.
Example 2:

Input: s = "cbbd"
Output: "bb"
 

Constraints:

1 <= s.length <= 1000
s consist of only digits and English letters.

"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
      s = list(s)

      res = []

      def extend(start, end):
        while start >= 0 and end < len(s) and s[start] == s[end]:
          start -= 1
          end += 1

        return s[start+1:end]

      for i in range(len(s)):
        odd = extend(i, i)
        even = extend(i, i + 1)

        if len(res) < len(odd):
          res = odd

        if len(res) < len(even):
          res = even

      return "".join(res)

        
        


