# Time Complexity: O(n log n + m log m)
# Space Complexity: O(1)
# Greedy
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
      g.sort()
      s.sort()

      res = 0
      i = 0

      for cookie in s:
        if cookie >= g[i]:
          res += 1
          i += 1

          if i == len(g):
            break

      return res

# Time Complexity: O(n log n + m log m)
# Space Complexity: O(1)
# Greedy

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
      g.sort()
      s.sort()

      res = 0
      i = 0
      j = 0

      while i < len(g) and j < len(s):
        if s[j] >= g[i]:
          res += 1
          i += 1

        j += 1

      return res

"""
Are the arrays sorted?


QUEUE


"""
