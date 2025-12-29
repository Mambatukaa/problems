""""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.





"""
# TC: O(n)
# SC: O(n)
class Solution:
    def isValid(self, s: str) -> bool:

        # collect opening inside the stack
        # when closing comes compare with the first opening in stack
            # if they don't match or stack is emtpy return False

        dic = {
            "(": ")",
            "{": "}",
            "[": "]"
        }

        stack = []

        for ch in s:
            if ch in dic:
                stack.append(ch)
            else:
                if not stack or dic[stack.pop()] != ch:
                    return False

        return not stack
        
