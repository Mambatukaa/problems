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





x^n == (x^2)^n/2 if n is even

x * x^2^n-1/2

"""

# Binary exponentiation
class Solution:
    # Maximum recursion depth exceeded
    def myPow(self, x: float, n: int) -> float:
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        def pow(n):
            if n == 0:
                return 1

            if n < 0:
                return 1 / pow(-n)

            return x * pow(n - 1)

        # Time Complexity: O(log n)
        # Space Complexity: O(log n)
        def powII(x, n):
            if n == 0:
                return 1

            if n < 0:
                return 1 / powII(x, -n)

            if n % 2 == 1:
                return x * powII(x * x, (n-1)/2)

            return powII(x * x, n / 2)

        # Time Complexity: O(log n)
        # Space Complexity: O(1)
        # Iterative
        def powIII(x, n):
            if n == 0:
                return 1

            if n < 0:
                n = -n
                x = 1 / x

            res = 1

            while n != 0:
                if n % 2 == 1:
                    res *= x
                    n -= 1

                x *= x
                n /= 2

            return res

        return powIII(2, -9)


solution = Solution()
print("res", solution.myPow(2.0, 10))

# x = 2
