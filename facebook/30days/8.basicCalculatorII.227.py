"""

Given a string s which represents an expression, evaluate this expression and return its value.
The integer division should truncate toward zero.
You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 11 .
Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval).

Example 1:
    Input: s = "3+2*2"
    Output: 7

Example 2:
    Input: s = " 3/2"
    Output: 1

Example 3:
    Input: s = " 3+5 / 2"
    Output: 5




Constraints:
• 1 <= s. length <= 3 * 105)
• s consists of integers and operators ('+', *-', '**, */*) separated by some number of spaces.
• s represents a valid expression.
• All the integers in the expression are non-negative integers in the range [0, 231 - 1].
• The answer is guaranteed to fit in a 32-bit integer.

"""


class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # Stack
    def calculate(self, s: str) -> int:
        stack = []

        n = len(s)
        curr_number = 0
        operation = "+"

        for i in range(n):
            ch = s[i]

            if ch.isnumeric():
                curr_number = curr_number * 10 + int(ch)

            if ((ch != " " and not ch.isnumeric()) or i == n - 1) :
                if operation == "+":
                    stack.append(curr_number)
                elif operation == "-":
                    stack.append(-curr_number)
                elif operation == "*":
                    stack.append(stack.pop() * curr_number)
                else:
                    num1 = stack.pop()

                    if num1 < 0:
                        stack.append(-(-num1 // curr_number))
                    else:
                        stack.append(num1 // curr_number)

                operation = ch
                curr_number = 0

        res = 0
        while stack:
            res += stack.pop()

        return res

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    #
    def calculateII(self, s: str) -> int:
        n = len(s)

        res = 0
        last_num = 0
        curr_num = 0
        operation = "+"

        for i in range(n):
            char = s[i]

            if char.isnumeric():
                curr_num = curr_num * 10 + int(char)


            if ((char != " " and not char.isnumeric()) or i == n - 1):
                if operation in ["+", "-"]:
                    if operation == "-":
                        curr_num = -curr_num

                    res += last_num
                    last_num = curr_num

                elif operation in ["*", "/"]:

                    if operation == "/":
                        last_num = int(last_num / curr_num) 
                    else:
                        last_num *= curr_num

                curr_num = 0
                operation = char

        res += last_num
        return res


solution = Solution()
s = " 3+5 / 2 "
s = "12-2147483647"
s = "14-3/2"


print("res:", solution.calculateII(s))
