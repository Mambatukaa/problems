# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Extend
def longestPalindrome(s):
  res = ""
  n = len(s)

  for i in range(len(s)):
    left = i
    right = i

    # odd length
    while left >= 0 and right < n and s[left] == s[right]:

      if len(res) < right - left + 1:
        res = s[left:right + 1]

      left -= 1
      right += 1

    left = i
    right = i + 1

    # even length
    while left >= 0 and right < n and s[left] == s[right]:

      if len(res) < right - left + 1:
        res = s[left:right + 1]

      left -= 1
      right += 1


  return res

s = "a"
print("res:", longestPalindrome(s))

"""

Given a string s, return the longest palindromic substring in s.


Example 1:
  Input:
    s = "babad"
  Output:
    "bab", "aba"

Example 2:
  Input:
    s = "cbbd"
  Output:
    "bb"



********************

Start to compare left and right sides
  If two sides are the same update the counter





"""
