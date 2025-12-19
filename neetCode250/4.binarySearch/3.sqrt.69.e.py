"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
 

Constraints:

0 <= x <= 231 - 1
"""

# TC: O(log n)
# SC: O(1)
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x

        l = 2
        r = x // 2

        while l <= r:
            mid = l + (r - l) // 2
            num = mid * mid

            if num == x:
                return mid
            elif num > x:
                # go left
                r = mid - 1
            else:
                # go right
                l = mid + 1
            
        return r



"""
x = 8

      L
      M
    R
1 2 3 4 5 6 7 8 9 10
"""

