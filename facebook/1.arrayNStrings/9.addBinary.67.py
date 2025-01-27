""""

Given two binary strings a and b, return their sum as a binary string.

Example 1:
    Input: a = "11", b = "1"
    Output: "100"

Example 2:
    Input: a = "1010", b = "1011"
    Output: "10101"

Constraints:
• 1 <= a. length, b. length <= 104
• a and b consist only of '0' or '1' characters.
• Each string does not contain leading zeros except for the zero itself.

"""


class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def addBinary(self, a: str, b: str) -> str:
        # replace a with the longest string
        if len(b) > len(a):
            a, b = b, a

        a = list(a)
        b = list(b)

        res = [0] * (len(a) + 1)

        carry = 0
        for i in range(1, len(a) + 1):
            num1 = int(a[-i])
            num2 = int(b[-i]) if i <= len(b) else 0

            total = carry + num1 + num2
            carry = total // 2 
            digit = total % 2

            res[-i] = str(digit)

        if carry == 1:
            res[0] = str(carry)

            return "".join(res)
        
        return "".join(res[1:])

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def addBinaryII(self, a: str, b: str) -> str:
        res = ""
        carry = 0

        a, b = a[::-1], b[::-1]

        for i in range(max(len(a), len(b))):
            digitA = int(a[i]) if i < len(a) else 0
            digitB = int(b[i]) if i < len(b) else 0

            total = carry + digitA + digitB
            digit = str(total % 2)
            res = digit + res
            carry = total // 2

        if carry == 1:
            res = "1" + res

        return res





solution = Solution()

a = "1010"
b = "1011"

print("res:", solution.addBinaryII(a, b))
