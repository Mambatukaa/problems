
""""
You are given a string s consisting of lowercase English letters. A duplicate removal consists of choosing two adjacent and equal letters and removing them.

We repeatedly make duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made. It can be proven that the answer is unique.

 

Example 1:

Input: s = "abbaca"
Output: "ca"
Explanation: 
For example, in "abbaca" we could remove "bb" since the letters are adjacent and equal, and this is the only possible move.  The result of this move is that the string is "aaca", of which only "aa" is possible, so the final string is "ca".
Example 2:

Input: s = "azxxzy"
Output: "ay"
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.

"""



# Time Complexity: O(n)
# Space Complexity: O(n - d) d: duplicates
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []

        for letter in s:
            if stack and stack[-1] == letter:
                stack.pop()
            else:
                stack.append(letter)


        return "".join(stack)
        


s = "abbbacxdd"
# cx
# Remove all duplicates
class Solution:
    def removeDuplicates(self, s: str) -> str:
        n = len(s)
        i = 0
        stack = []

        while i < n:
            if stack and stack[-1] == s[i]: 
                while i < n and stack[-1] == s[i]:
                    i += 1
                stack.pop()

            else:
                stack.append(s[i])
                i+= 1


        return "".join(stack)

# remove k
class Solution:
    def removeDuplicates(self, s: str, k) -> str:
        n = len(s)
        i = 0
        stack = []

        for letter in s:
            if stack and stack[-1][0] == letter:
                stack[-1][1] += 1

            else:
                stack.append([letter, 1])

            if stack[-1][1] == k:
                stack.pop()

        res = []

        for letter, count in stack:
            res.append(letter * count)
        return "".join(res)


#            i
s = "abbbaacxddd"
solution = Solution()
print("res:", solution.removeDuplicates(s, 1))
# cx
