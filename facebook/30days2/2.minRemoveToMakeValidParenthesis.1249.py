class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def minRemoveToMakeValid(self, s: str) -> str:
        valid = set()
        opening = []

        for i in range(len(s)):
            ch = s[i]
            if ch == "(":
                opening.append(i) 
            elif ch == ")":
                if opening:
                    valid.add(opening.pop())
                    valid.add(i)
            
        res = ""

        for i in range(len(s)):
            ch = s[i]

            if ch == "(" or ch == ")":
                if i in valid:
                    res += ch
            else:
                res += ch

        return res
        
class Solution:
    # Time Complexity: O(4n)
    # Space Complexity: O(n)
    # Using stack and string builder
    def minRemoveToMakeValid(self, s: str) -> str:
        indexes_to_remove = set()
        stack = []

        for i, c in enumerate(s):
            if c not in "()":
                continue
            if c == "(":
                stack.append(i)
            elif not stack:
                indexes_to_remove.add(i)
            else:
                stack.pop()

        indexes_to_remove = indexes_to_remove.union(set(stack))

        res = []

        for i, c in enumerate(s):
            if i not in indexes_to_remove:
                res.append(c)

        return "".join(res)

# Time Complexity: O(2n)
# Space Complexity: O(n)
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = []

        balance = 0
        open_seen = 0

        for c in s:
            if c == "(":
                balance += 1
                open_seen += 1
            elif c == ")":
                if not balance:
                    continue

                balance -= 1
            res.append(c)

        filtered = []
        open_to_keep = open_seen - balance

        # Pass 2: Remove the rightmost "("
        for c in res:
            if c == "(":
                open_to_keep -= 1
                if open_to_keep < 0:
                    continue
            filtered.append(c)        

        return "".join(filtered)
                



"""
Make the string valid removing minimum parentheses


s = lee(t(c)o)de) ---> lee(t(c)o)de


s = a)b(c)d --> ab(c)d

s = "))(("


1. Is parenthesis are valid or not


    s = a)b(c)d

    res = ""

    validParenthesis = set()
    first iteration:
        save the valid parenthesis using stack

            if curr == "(":
                opening.append(index)
            if curr == ")":
                if opening:
                    validParenthesis.add(opening.pop())
                    validParenthesis.add(index)

    second iteration:
        if curr == "(" or curr == ")":
            if index in validParenthesis:
                add to the res
        res += curr



        





"""
# variant
class Solution:
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

