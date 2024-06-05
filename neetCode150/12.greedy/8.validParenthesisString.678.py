# Time Complexity: O(n)
# Space Complexity: O(1)
# Greedy solution
class Solution:
    def checkValidString(self, s: str) -> bool:
      leftMin = 0
      leftMax = 0

      for ch in s:
        if ch == "*":
          leftMin = max(0, leftMin - 1)
          leftMax += 1
        elif ch == ")":
          leftMin = max(0, leftMin - 1)
          leftMax -= 1
        else:
          leftMin += 1
          leftMax += 1


      print(leftMin, leftMax)

      return leftMin == 0 and leftMax >= 0



solution = Solution()
print(solution.checkValidString("((*)"))
# *** *** *** * 


"""

Count the possibility of leftMin and leftMax



"""
