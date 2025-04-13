""""





A digit string is good if the digits (0-indexed) at even indices are even and the digits at odd indices are prime (2, 3, 5, or 7).

For example, "2582" is good because the digits (2 and 8) at even positions are even and the digits (5 and 2) at odd positions are prime. However, "3245" is not good because 3 is at an even index but is not even.
Given an integer n, return the total number of good digit strings of length n. Since the answer may be large, return it modulo 109 + 7.

A digit string is a string consisting of digits 0 through 9 that may contain leading zeros.

 

Example 1:

Input: n = 1
Output: 5
Explanation: The good numbers of length 1 are "0", "2", "4", "6", "8".
Example 2:

Input: n = 4
Output: 400
Example 3:

Input: n = 50
Output: 564908303
 

Constraints:

1 <= n <= 10^15


"""

class Solution:
    # Time Limit exceeded
    def countGoodNumbers(self, n: int) -> int:
        if n == 1:
            return 5

        even = odd = n // 2

        if n % 2:
            even = odd + 1

        res = (5 ** even) * (4 ** odd)

        return res % limit

class Solution:
    # Time Complexity: O(log n)
    def countGoodNumbers(self, n: int) -> int:
        mod = 10**9 + 7

        # use fast exponentiation to calculate x^y % mod
        def quickmul(x: int, y: int) -> int:
            res = 1

            while y > 0:
                # is odd
                if y % 2:
                    res = res * x % mod

                x *= x % mod
                y = y // 2

            return res

        return quickmul(5, (n + 1) // 2) * quickmul(4, n // 2) % mod
        
    

solution = Solution()

print("res:", solution.countGoodNumbers(50))

"""

even positions must be even
odd positions are prime (2, 3, 5, 7)

n = 2

02
03
05
07

2
4
6
8



n = 1 = 5
n = 2 = 20
n = 3 = 100
n = 4 = 400

even digit == 5 options
odd digit == 4 options

n = 1 ==> 5
n = 2 ==> 5 * 4
n = 3 ==> 5 * 4 * 5 => odd = 1 even == 2
n = 10 ==> 5 * 4 * 5 * 4 * 5 * 4 * 5 * 4 * 5 * 4



if n is even the even and odd digits are the same
    n / 2 == odd | even

else:
    odd = n // 2
    even = odd + 1


"""
