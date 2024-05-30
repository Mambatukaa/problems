# Time Complexity: O(n)
# Space Complexity: O(1)
# Greedy
class Solution:
    def sumOfDigits(self, n):
      return sum([int(i) for i in str(n)])

    def makeIntegerBeautiful(self, n: int, target: int) -> int:
      i = 0
      curr = n

      while self.sumOfDigits(n) > target:
        n //= 10
        n += 1
        i += 1
      
      return n * (10 ** i) - curr




"""

two positive N and TARGET.

beautiful if the SUM OF DIGITS is less than or equal to TARGET.


return MIN NON-NEGATIVE INTEGER X such that N + X is BEAUTIFUL. 
  * Always possible to make n beautiful.


Example 1. 
  n = 16,
  target = 6

  initial sum of digits = 1 + 6 = 7 > target..... 

  1. Calculate the sum of DIGITS
  2. Compare the digits to target

    curr = n

    if target >= sumOfDigits(curr):
      return curr - n 
    else:
  

  n = 467
  target = 10 

  4 + 6 + 7 = 17 INVALID
  4 + 7 + 0 = 11 INVALID
  5 + 0 + 0 = 5 VALID

*********************************************

if curr is invalid update curr to change [i]

create list of digits to better calculation and change






"""
