""""
Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
 

Constraints:

-100.0 < x < 100.0
-231 <= n <= 231-1
n is an integer.
Either x is not zero or n > 0.
-104 <= xn <= 104








"""

# Upgrade the x
# Time Complexity: O(log n)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        negative = False
        if n < 0:
            n = -n
            negative = True
        res = 1
        
        while n != 0:
            if n % 2:
                res *= x
                n -= 1
            x *= x
            n /= 2

        return res if not negative else 1 / res
class Solution:
    def myPow(self, x: float, n: int) -> float:
        def pow(x, n):
            if n == 0:
                return 1
            
            if n < 0:
                return 1 / pow(x, -n)

            if n % 2:
                return x * pow(x * x, (n - 1 // 2))

            return pow(x * x, n // 2)

        return pow(x, n)

       

"""
Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000



1. Naive approach

    result = multiple x n times

    if the n is negative:
        1 / result 


    # Time Complexity: O(n)


x = 3, n = 10

Upgrade x and update the answer until n reaches 0
    1. If n is odd update the res by x and decrement n by 1

3^10
9^4 * (9^1 update the answer):
81^2 
59049^1 (59049 update the answer)

1   2   3   4   5   6   7   8   9   10
3 * 3 * 3 * 3 * 3 * 3 * 3 * 3 * 3 * 3

9 * 9 * 9 * 9 * 9

81 * 81 * 9

if n == odd:
    res *= x
    n -= 1




memo = { }




"""
