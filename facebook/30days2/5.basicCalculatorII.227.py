""""
Given a string s which represents an expression, evaluate this expression and return its value. 

The integer division should truncate toward zero.

You may assume that the given expression is always valid. All intermediate results will be in the range of [-231, 231 - 1].

Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().

 

Example 1:

Input: s = "3+2*2"
Output: 7
Example 2:

Input: s = " 3/2 "
Output: 1
Example 3:

Input: s = " 3+5 / 2 "
Output: 5
 

Constraints:

1 <= s.length <= 3 * 105
s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
s represents a valid expression.
All the integers in the expression are non-negative integers in the range [0, 231 - 1].
The answer is guaranteed to fit in a 32-bit integer.

"""
class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    # where n is the length of the string s
    # https://leetcode.com/problems/basic-calculator-ii/description/

    def calculate(self, s: str) -> int:
        # add on the stack on addition and substraction
        stack = []

        operation = "+"
        curr_num = 0

        n = len(s)
        for i in range(n):
            ch = s[i]

            if ch.isdigit():
                curr_num = curr_num * 10 + int(ch)
            if ((ch != " " and not ch.isdigit()) or i == n - 1) :
                if operation == "+":
                    stack.append(curr_num)
                elif operation == "-":
                    stack.append(-curr_num)
                elif operation == "*":
                    stack.append(stack.pop() * curr_num)
                else:
                    stack.append(int(stack.pop() / curr_num))

                operation = ch
                curr_num = 0
        
        res = 0

        for num in stack:
            res += num

        return res

"""
num = 2

operation *:
    last_num = last_num * curr_num


_num
                    else:
                        last_num = int(last_num / curr_num)

                operation = ch
                curr_num = 0
        
        res += last_num
        return res


track curr_num and last_num

if the curr_char is + or -:
    update the res and update the last_num

if the curr_Char is * or /:
    update the last num not response



3 + 2 * 2

curr_num = 0
last_num = 0
operation = +

-----------------------------------------------

curr_num = 3

ch = +

operation == +
    res += last_num = 0
    last_num = 3
    operation = +
-------------------------------------------------------

curr_num = 2

ch = *

res += 3
last_num = 2

operation = *


-------------------------------------------------------
curr_num = 2
last_class Solution:
    def calculate(self, s: str) -> int:
        # add on the stack on addition and substraction
        operation = "+"
        last_num = 0
        curr_num = 0
        res = 0

        n = len(s)
        for i in range(n):
            ch = s[i]

            if ch.isdigit():
                curr_num = curr_num * 10 + int(ch)

            if ((ch != " " and not ch.isdigit()) or i == n - 1) :
                if operation in "+-":
                    # update the res
                    if operation == "-":
                        curr_num = -curr_num

                    res += last_num
                    last_num = curr_num
                else:
                    if operation == "*":
                        last_num = last_num * curr

"""


"""

35 + 2 * 2


+
35

current_number
current_char
operation = 


track curr_char

if curr_char is operation:

    operation == +:
        add curr_num to the stack
    operation == -:
        add -curr_num to the stack
    operation == *:
        res = stack.pop() * curr_num
        add res to the stack

    operation == /:
        res = stack.pop() // curr_num
        add res to the stack


    
    update the operation and

else:
    update the curr_number



"""


class Solution:
    def calculate(self, s: str) -> int:
        # add on the stack on addition and substraction
        operation = "+"
        last_num = 0
        curr_num = 0
        res = 0

        n = len(s)
        for i in range(n):
            ch = s[i]

            if ch.isdigit():
                curr_num = curr_num * 10 + int(ch)

            if ((ch != " " and not ch.isdigit()) or i == n - 1) :
                if operation in "+-":
                    # update the res
                    if operation == "-":
                        curr_num = -curr_num

                    res += last_num
                    last_num = curr_num
                else:
                    if operation == "*":
                        last_num = last_num * curr_num
                    else:
                        last_num = int(last_num / curr_num)

                operation = ch
                curr_num = 0
        
        res += last_num
        return res

"""

track curr_num and last_num

if the curr_char is + or -:
    update the res and update the last_num

if the curr_Char is * or /:
    update the last num not response



3 + 2 * 2

curr_num = 0
last_num = 0
operation = +

-----------------------------------------------

curr_num = 3

ch = +

operation == +
    res += last_num = 0
    last_num = 3
    operation = +
-------------------------------------------------------

curr_num = 2

ch = *

res += 3
last_num = 2

operation = *


-------------------------------------------------------
curr_num = 2
last_num = 2

operation *:
    last_num = last_num * curr_num


"""
