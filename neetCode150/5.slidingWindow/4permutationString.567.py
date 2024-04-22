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


# Time Complexity: O(n)
# Space Complexity: O(1)
class Solution1:
    def checkInclusion(self, s1: str, s2: str) -> bool:
      # base case
      if len(s1) > len(s2):
        return False

      n = len(s1)
      m = len(s2)

      s1_counts = [0] * 26
      s2_counts = [0] * 26

      for i in range(len(s1)):
          s1_counts[ord(s1[i]) - ord('a')] += 1
          s2_counts[ord(s2[i]) - ord('a')] += 1
      
      if(s1_counts == s2_counts):
          return True
        
      start = 0

      for j in range(n, m):
          s2_counts[ord(s2[j]) - ord('a')] += 1

          s2_counts[ord(s2[start]) - ord('a')] -= 1

          if(s1_counts == s2_counts):
              return True

          start += 1
          
      return False

solution = Solution1()

s1 = 'ab'
s2 = 'eidbaooo'

print(solution.checkInclusion(s1, s2))

# Time Complexity: O(n)
# Space Complexity: O(1)
# Solution of NeetCode
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
      if(len(s1) > len(s2)):
        return False

      s1Counts, s2Counts = [0] * 26, [0] * 26

      for i in range(len(s1)):
        s1Counts[ord(s1[i]) - ord('a')] += 1
        s2Counts[ord(s2[i]) - ord('a')] += 1

      matches = 0

      for i in range(26):
        matches += 1 if s1Counts[i] == s2Counts[i] else 0

      l = 0

      for r in range(len(s1), len(s2)):
        if matches == 26: return True

        index = ord(s2[r]) - ord('a')
        s2Counts[index] += 1

        if s1Counts[index] == s2Counts[index]:
          matches += 1
        elif s1Counts[index] + 1 == s2Counts[index]:
          matches -= 1

        index = ord(s2[l]) - ord('a')
        s2Counts[index] -= 1

        if s1Counts[index] == s2Counts[index]:
          matches += 1
        elif s1Counts[index] - 1 == s2Counts[index]:
          matches -= 1

        l += 1
      
      return matches == 26

