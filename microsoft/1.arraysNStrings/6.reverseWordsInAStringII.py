class Solution:

  def reverse(self, s, l, r):
    # reverse the array
    while l < r:
      s[l], s[r] = s[r], s[l]
      l += 1
      r -= 1

  # Time Complexity: O(n), it's two passes along the string
  # Space Complexity: O(1)
  def reverseWords(self, s):
    """
    Do not return anything, modify s in-place instead.
    """

    n = len(s)

    self.reverse(s, 0, n - 1)

    # find words and reverse
    start = 0
    end = 0

    while start < n:
      while end < n and s[end] != " ":
        end += 1

      self.reverse(s, start, end - 1)

      start = end = end + 1


solution = Solution()

s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]


solution.reverseWords(s)

print("res:", s)



"""
Given a character array s, reverse the order of the words.
A word is defined as a sequence of non-space characters. The words in s will be separated by a single space.
Your code must solve the problem in-place, i.e. without allocating extra space.



1. Reverse the entire array.
2. Find the words and reverse the words one by one. Until reaches the limit.

"""
