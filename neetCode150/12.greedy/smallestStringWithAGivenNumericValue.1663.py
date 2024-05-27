# Greedy
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
      res = [""] * n

      remaining = k

      for i in range(len(res) - 1, -1, -1):
        possibleMaxEl = min(remaining - i, 26)

        res[i] = chr(96 + possibleMaxEl)

        remaining -= possibleMaxEl

      return ''.join(i for i in res)


"""
Input: n = 3, k = 27

Output: "aay"

Explanation: The numeric value of the string is 1 + 1 + 25 = 27


Make 27 using 3 numbers. Numbers range must be 1 to 26. Numbers can be duplicate



"""
