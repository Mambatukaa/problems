""""



You are given a string s.
Your task is to remove all digits by doing this operation repeatedly:
• Delete the first digit and the closest non-digit character to its left.
Return the resulting string after removing all digits.

Example 1:
    Input: s = "abc"
    Output: "abc"
    Explanation:
    There is no digit in the string.

Example 2:
    Input: s = "cb34"
    Output: ""
    Explanation:
    First, we apply the operation on s [2], and s becomes "с4".
    Then we apply the operation on s [1], and s becomes '''.

Constraints:
    • 1 <= s. length <= 100
    • s consists only of lowercase English letters and digits.
    • The input is generated such that it is possible to delete all digits.

"""


class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def clearDigits(self, s: str) -> str:
        stack = []

        for ch in s:
            if not ch.isnumeric():
                stack.append(ch)
            else:
                stack.pop()


        return "".join(stack)   

    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def clearDigitsII(self, s):
        res = []
        delete_cnt = 0

        for i in reversed(range(len(s))):
            if s[i].isnumeric():
                delete_cnt += 1
            elif delete_cnt:
                delete_cnt -= 1
            else:
                res.append(s[i])

        return "".join(res[::-1])

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    # In-place
    def clearDigitsIII(self, s):
        s = list(s)
        answer_length = 0

        for i in range(len(s)):
            if s[i].isnumeric():
                answer_length = max(answer_length - 1, 0)
            else:
                s[answer_length] = s[i]
                answer_length += 1

        s = s[:answer_length]

        return "".join(s)

solution = Solution()

print("res:", solution.clearDigitsIII("abc111"))
