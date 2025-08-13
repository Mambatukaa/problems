""""
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.

 

Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"
Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"
Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"
 

Constraints:

1 <= num1.length, num2.length <= 104
num1 and num2 consist of only digits.
num1 and num2 don't have any leading zeros except for the zero itself.








"""

# Time Complexity: O(max(n1, n2))
# Space Complexity: O(max(n1, n2))
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        p1 = len(num1) - 1
        p2 = len(num2) - 1 

        carry = 0

        res = []

        while carry or p1 >= 0 or p2 >= 0:
            val1 = ord(num1[p1]) - ord('0') if p1 >= 0 else 0
            val2 = ord(num2[p2]) - ord('0') if p2 >= 0 else 0

            total = val1 + val2 + carry
            carry = total // 10

            res.append(str(total % 10))

            p1 -= 1
            p2 -= 1

        return "".join(res[::-1])

