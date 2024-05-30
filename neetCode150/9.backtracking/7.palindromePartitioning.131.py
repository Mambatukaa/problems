class Solution:
    def partition(self, s):
        res = []
        part = []

        def backtracking(i):
            if i >= len(s):
                res.append(part.copy())
            
            for j in range(i, len(s)):
                if self.isPalindrome(s, i, j):
                    part.append(s[i:j+1])
                    backtracking(j + 1)
                    part.pop()
      
        backtracking(0)

        return res


    def isPalindrome(self, s, l, r):
        while l <= r:
          if s[l] != s[r]:
            return False
          l += 1
          r -= 1

        return True

        
solution = Solution()

print(solution.partition("aab"))
