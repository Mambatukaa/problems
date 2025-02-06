""""


Given a string s of '(', ') ' and lowercase English characters.
Your task is to remove the minimum number of parentheses ('"' or ')' , in any positions) so that the resulting
parentheses string is valid and return any valid string.
Formally, a parentheses string is valid if and only if:
• It is the empty string, contains only lowercase characters, or
• It can be written as AB (A concatenated with B), where A and B are valid strings, or
• It can be written as (A) , where A is a valid string.


Example 1:
    Input: s = "'lee(t(c)o) de)"
    Output: "lee(t(c)o) de"
    Explanation: "lee(t(co)de)", "lee(t(c)ode)" would also be accepted.
Example 2:
    Input: s = "a)b(c)d"
    Output: "ab(c)d"

Example 3:
    Input: s = "))(("
    Output: "'
    Explanation: An empty string is also valid.

Constraints:
• 1 < s. length <= 10^5
• s [i] is either '(' , ')', or lowercase English letter.


"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        openingIdx = []
        closingIdx = []

        for i in range(len(s)):
            ch = s[i]

            if ch == "(":
                openingIdx.append(i)
            elif ch == ")":
                if openingIdx:
                    openingIdx.pop()
                else:
                    closingIdx.append(i)

        skipSet  = set(openingIdx + closingIdx)

        res = ""

        for i in range(len(s)):
            if i not in skipSet:
                res += s[i]



        return res

    def minRemoveToMakeValidII(self, s: str) -> str:
        openingSeen = 0
        balance = 0
        firstPassChars = []

        for ch in s:
            if ch == "(":
                balance += 1
                openingSeen += 1
            elif ch == ")":
                if not balance:
                    continue

                balance -= 1

            firstPassChars.append(ch)

        openingKeep = openingSeen - balance

        res = []

        for ch in firstPassChars:
            if ch == "(":
                openingKeep -= 1

                if openingKeep < 0:
                    continue

            res.append(ch)

        return "".join(res)




solution = Solution()

s = "lee(t(c)o)de)"

print("res:", solution.minRemoveToMakeValidII(s))
        
