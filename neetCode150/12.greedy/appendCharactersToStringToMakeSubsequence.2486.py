# Time Complexity: O(s)
# Space Complexity: O(1)
# Greedy
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
      # use two pointers method
      # make s subsequence of t

      sArr = list(s)
      tArr = list(t)

      sPointer = 0
      tPointer = 0

      while sPointer < len(sArr) and tPointer < len(tArr):
        sItem = sArr[sPointer]
        tItem = tArr[tPointer]

        if sItem == tItem:
          tPointer += 1

        sPointer +=1
      
      return len(tArr) - tPointer
    
    def appendCharactersII(self, s, t):
      i = 0

      for c in s:
        if c == t[i]:
          i += 1
          
          if i >= len(t):
            return 0

      return len(t) - i



solution = Solution()

print(solution.appendCharacters("coaching", "c"))

"""


minimum number of characters that neet to be appended to the end of s so that t becomes subsequence of t.



     **
s = "coaching"

     **
t = "coding"


find the current subsequence from S using T

save the last index of the subsequence. For above example.

  t's 1 idx is the last index. So we need to APPEND idx + 1 to length - 1.


"""
