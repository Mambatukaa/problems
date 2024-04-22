#initial

# Time Complexity: O(26 * O(n) * O(m)) m = len(s1) n = len(s2)
# Space Complexity: O(1)
# 20 minutes
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
      if len(s1) > len(s2):
        return False

      s1Map = [0] * 26

      for ch in s1:
        s1Map[ord(ch) - ord('a')] += 1

      def isValid(l, r):
          clone = s1Map[:]

          substring = s2[l: r + 1]

          # O(m)
          for ch in substring:
              clone[ord(ch) - ord('a')] -= 1

          
          for item in clone:
            if item != 0:
                return False
          
          return True

      
      n = len(s2)
      m = len(s1)
      l = 0

      # O(n)
      for r in range(n):
          if r - l + 1 >= m:
              # substring reaches the limit check isValid
              if isValid(l, r):
                  return True
              l += 1
          

      return False


solution = Solution()

s1 = 'ab'
s2 = 'eidbaooo'

print(solution.checkInclusion(s1, s2))
