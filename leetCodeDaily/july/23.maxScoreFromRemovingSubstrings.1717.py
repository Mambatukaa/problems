"""
You are given a string s and two integers x and y. You can perform two types of operations any number of times.

Remove substring "ab" and gain x points.
For example, when removing "ab" from "cabxbae" it becomes "cxbae".
Remove substring "ba" and gain y points.
For example, when removing "ba" from "cabxbae" it becomes "cabxe".
Return the maximum points you can gain after applying the above operations on s.

 

Example 1:

Input: s = "cdbcbbaaabab", x = 4, y = 5
Output: 19
Explanation:
- Remove the "ba" underlined in "cdbcbbaaabab". Now, s = "cdbcbbaaab" and 5 points are added to the score.
- Remove the "ab" underlined in "cdbcbbaaab". Now, s = "cdbcbbaa" and 4 points are added to the score.
- Remove the "ba" underlined in "cdbcbbaa". Now, s = "cdbcba" and 5 points are added to the score.
- Remove the "ba" underlined in "cdbcba". Now, s = "cdbc" and 5 points are added to the score.
Total score = 5 + 4 + 5 + 5 = 19.
Example 2:

Input: s = "aabbaaxybbaabb", x = 5, y = 4
Output: 20
 

Constraints:

1 <= s.length <= 105
1 <= x, y <= 104
s consists of lowercase English letters.






"""
    
# Stack
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        self.score = 0
        s = list(s)

        def removeSubstring(s, score, substr):
            stack = []

            for char in s:
                if stack and stack[-1] + char == substr:
                    stack.pop()
                    self.score += score
                else:
                    stack.append(char)

            return stack

        if x > y:
            stack = removeSubstring(s, x, "ab")
            removeSubstring(stack, y, "ba")
        else:
            stack = removeSubstring(s, y, "ba")
            removeSubstring(stack, x, "ab")

        return self.score
        

        





"""
x = points "ab"
y = points "ba"


cdbcbbaaabab



"""
    
