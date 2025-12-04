"""
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

# Time Complexity: O(log n)
# Space Complexity: O(1)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n *= -1

        res = 1

        while n != 0:
            if n % 2:
                res *= x
                n -= 1

            x *= x
            n //= 2

        return res



# Time Complexity: O(log n)
# Space Complexity: O(log n)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        

        def rec(x, n):
            if n == 0:
                return 1

            if n < 0: 
                return 1 / rec(x, -n)

            if n % 2:
                return x * rec(x * x, (n - 1) // 2)
            
            return rec(x * x, n // 2)


    
        return rec(x, n)

"""

2^8 => 

4^4  => 4 * 4 * 4 * 4 => 256

16^2 => 






"""

        
        
