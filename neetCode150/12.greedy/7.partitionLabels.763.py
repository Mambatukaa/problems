# Time Complexity: O(n)
# Space Complexity: O(1) HASHMAP has maximum 26 elements
# Greedy
class Solution:
    def partitionLabels(self, s: str):

      dic = {}

      for i in range(len(s)):
        dic[s[i]] = i
      
      
      size = 0
      lastIdx = 0

      res = []

      for i in range(len(s)):
        size += 1
        lastIdx = max(lastIdx, dic[s[i]])

        if lastIdx == i:
          res.append(size)
          size = 0

      return res


solution = Solution()

solution.partitionLabels("caedbdedda")
