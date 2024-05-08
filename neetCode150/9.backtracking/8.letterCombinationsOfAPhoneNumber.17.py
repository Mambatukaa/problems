# Time Complexity: O(n * 4^n) n = digits.length
# Space Complexity: O(n * 4^n)
# 20 minutes
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
      digitsMap = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
      }

      res = []

      def backtracking(curr, start):
        if len(curr) == len(digits):
          res.append(curr)
          return

        for letter in digitsMap[digits[start]]:
          curr += letter
          backtracking(curr, start + 1)
          curr = curr[:-1]
      
      if digits:
        backtracking("", 0)
      
      return res
        
