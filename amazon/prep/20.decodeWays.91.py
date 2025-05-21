""""
You have intercepted a secret message encoded as a string of numbers. The message is decoded via the following mapping:

"1" -> 'A'

"2" -> 'B'

...

"25" -> 'Y'

"26" -> 'Z'

However, while decoding the message, you realize that there are many different ways you can decode the message because some codes are contained in other codes ("2" and "5" vs "25").

For example, "11106" can be decoded into:

"AAJF" with the grouping (1, 1, 10, 6)
"KJF" with the grouping (11, 10, 6)
The grouping (1, 11, 06) is invalid because "06" is not a valid code (only "6" is valid).
Note: there may be strings that are impossible to decode.

Given a string s containing only digits, return the number of ways to decode it. If the entire string cannot be decoded in any valid way, return 0.

The test cases are generated so that the answer fits in a 32-bit integer.

 

Example 1:

Input: s = "12"

Output: 2

Explanation:

"12" could be decoded as "AB" (1 2) or "L" (12).

Example 2:

Input: s = "226"

Output: 3

Explanation:

"226" could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Example 3:

Input: s = "06"

Output: 0

Explanation:

"06" cannot be mapped to "F" because of the leading zero ("6" is different from "06"). In this case, the string is not a valid encoding, so return 0.

 

Constraints:

1 <= s.length <= 100
s contains only digits and may contain leading zero(s).






"""


class Solution:
    # Top down approach
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def numDecodings(self, s: str) -> int:
        n = len(s)

        dp = {
            n: 1
        }

        def backtracking(i):
            if i in dp:
                return dp[i]

            if s[i] == "0":
                return 0

            # go with one digit
            res = backtracking(i + 1)

            # go with two digits if it's possible
            if (i + 1 < n and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456")):
                res += backtracking(i + 2)

            dp[i] = res
            return res
                
        return backtracking(0)
    # Bottom up
    def numDecodingsII(self, s: str) -> int:
        if s[0] == "0":
            return 0
        n = len(s)
        dp = {
            n: 1
        }

        for i in range(n - 1, -1, -1):
            # one digit
            dp[i] = 0
            if 0 < int(s[i]) <= 9:
                dp[i] = dp[i + 1]

            # two digits
            if (i + 1 < n) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                # try with two digits
                dp[i] += dp[i + 2]

        return dp[0]

    def numDecodingsIII(self, s: str) -> int:
        if s[0] == "0":
            return 0

        n = len(s)

        dp = [0] * (n + 1)

        dp[0], dp[1] = 1, 1

        for i in range(2, n + 1):
            one_digit = int(s[i - 1])

            if 0 < one_digit <= 9:
                dp[i] = dp[i - 1]

            two_digit = int(s[i - 2: i])

            if 10 <= two_digit <= 26:
                dp[i] += dp[i - 2]

        return dp[-1]

    def numDecodingsIV(self, s: str) -> int:
        if s[0] == "0":
            return 0

        n = len(s)

        first = 1
        second = 1

        for i in range(2, n + 1):
            temp = 0
            one_digit = int(s[i - 1])

            if 0 < one_digit <= 9:
                temp = second

            two_digit = int(s[i - 2: i])

            if 10 <= two_digit <= 26:
                temp += first

            first = second
            second = temp

        return second




solution = Solution()

print("res:", solution.numDecodings("2207"))
print("res:", solution.numDecodingsIII("2207"))
print("res:", solution.numDecodingsIV("2207"))

