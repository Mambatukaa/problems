class Solution:
    def hammingWeight(self, n: int) -> int:
      res = 0

      while n:
        res += n % 2
        # shift every bit by one
        n = n >> 1
        # n = int(n / 2)

      return res 

    def hammingWeightII(self, n: int) -> int:
      res = 0

      while n:
        n = n & (n - 1)
        res += 1

      return res

solution = Solution()
        
print(solution.hammingWeightII(128))

"""

"""
