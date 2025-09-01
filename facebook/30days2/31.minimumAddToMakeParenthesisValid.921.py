""""
A parentheses string is valid if and only if:

It is the empty string,
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
You are given a parentheses string s. In one move, you can insert a parenthesis at any position of the string.

For example, if s = "()))", you can insert an opening parenthesis to be "(()))" or a closing parenthesis to be "())))".
Return the minimum number of moves required to make s valid.

 

Example 1:

Input: s = "())"
Output: 1
Example 2:

Input: s = "((("
Output: 3
 

Constraints:

1 <= s.length <= 1000
s[i] is either '(' or ')'.






"""
# in place
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        
        opening_brackets = 0

        res = 0

        for ch in s:
            if ch == "(":
                opening_brackets += 1

            else:
                if opening_brackets == 0:
                    res += 1
                else:
                    opening_brackets -= 1

        return res + opening_brackets
                

class Solution:
    # in place
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)

        l = 0
        opens = 0
        total_opening = 0

        for r in range(len(s)):
            curr = s[r] 

            # swap current valid with left
            if curr == "(":
                total_opening += 1
                opens += 1
            elif curr == ")":
                if opens == 0:
                    continue
                opens -= 1

            s[l] = s[r]
            l += 1

        keep = total_opening - opens

        n = l
        l = 0

        for i in range(n):
            curr = s[i]

            if curr == "(":
                if keep == 0:
                    continue
                keep -= 1
            s[l] = s[i]
            l += 1


        return "".join(s[:l])

        
"""

keep = 0

    l      
()xa(a
     i


"""
class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def minRemoveToMakeValid(self, s: str) -> str:
        # (), [], {}
        """
        opening = {
            "(": 0,
            "[": 0,
            "{": 0
        }

        total = {

        }
        
        """
        pair = {
            "}": "{",
            ")": "(",
            "]": "[",
        }

        opening = defaultdict(int)
        total = defaultdict(int)

        temp = []

        for ch in s:
            if ch in pair:
                # pair[ch]
                if opening[pair[ch]] == 0:
                    continue
                opening[pair[ch]] -= 1
            elif ch in "({[": #opening
                opening[ch] += 1
                total[ch] += 1

            temp.append(ch)

        keep = {}

        for key in "{([":
            keep[key] = total[key] - opening[key]

        ans = []
        for ch in temp:
            if ch in keep:
                if keep[ch] == 0:
                    continue
                keep[ch] -= 1
            ans.append(ch)
        return "".join(ans)

