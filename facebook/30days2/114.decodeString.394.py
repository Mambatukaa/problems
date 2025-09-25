


"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed 105.

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"
Example 2:

Input: s = "3[a2[c]]"
Output: "accaccacc"
Example 3:

Input: s = "2[abc]3[cd]ef"
Output: "abcabccdcdcdef"
 

Constraints:

1 <= s.length <= 30
s consists of lowercase English letters, digits, and square brackets '[]'.
s is guaranteed to be a valid input.
All the integers in s are in the range [1, 300].
"""

# Stack
# TC: O(N * maxK^Countk)
# SC: O(N * maxK^CountK)


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch != "]":
                stack.append(ch)
            else:
                sub_str = ""

                while stack and stack[-1] != "[":
                    sub_str = stack.pop() + sub_str
                
                # pop opening square bracket
                stack.pop()

                k = ""

                while stack and stack[-1].isdigit():
                    k = stack.pop() + k

                stack.append(int(k) * sub_str)

        return "".join(stack)


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_num = 0
        curr_str = ""

        for ch in s:
            if ch == "[":
                stack.append(curr_str)
                stack.append(curr_num)
                curr_str = ""
                curr_num = 0

            elif ch == "]":
                num = stack.pop()
                prev_str = stack.pop()
                curr_str = prev_str + num * curr_str
            elif ch.isdigit():
                curr_num = curr_num * 10 + int(ch)
            else:
                curr_str += ch
        return curr_str




"""

stack = []


]
a
[
3





"""
class Solution:
    def decodeString(self, s: str) -> str:
        def helper(i: int) -> tuple[str, int]:
            res = ""
            num = 0

            while i < len(s):
                ch = s[i]

                if ch.isdigit():
                    num = num * 10 + int(ch)

                elif ch == "[":
                    # Recurse for the substring inside brackets
                    sub_str, i = helper(i + 1)
                    res += num * sub_str
                    num = 0  # reset after using

                elif ch == "]":
                    # Return current result and position
                    return res, i

                else:  # normal character
                    res += ch

                i += 1

            return res, i

        decoded, _ = helper(0)
        return decoded

