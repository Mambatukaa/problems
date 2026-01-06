""""
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

 

Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1
Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16
Example 3:

Input: n = 3
Output: false
 

Constraints:

-231 <= n <= 231 - 1
 

Follow up: Could you solve it without loops/recursion?
"""

class Solution:
    # Time Complexity: O(log n)
    # Space Complexity: O(1)
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False


        while n % 2 == 0:
            n /= 2


        return n == 1



solution = Solution()
print("res:", solution.isPowerOfTwo(10))
"""

2^0 = 1
2^1 = 2
2^2 = 4
2^3 = 8
2^4 = 16
2^5 = 32
2^6 = 64


6 ==> 3 ===> 1 ==> 0


"""

