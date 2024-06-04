# Time Complexity: O(n)
# Space Complexity: O(1) HASHMAP has maximum 26 elements
# Greedy
class Solution:
    def partitionLabels(self, s: str):

      dic = {}

      for i, val in enumerate(s):
        dic[val] = i
      
      res = []
      size, end = 0, 0

      for i, val in enumerate(s):
        size += 1
        end = max(end, dic[val])

        if end == i:
          res.append(size)
          size = 0

      return res


solution = Solution()

print(solution.partitionLabels("caedbdedda"))
