"""

Given two strings s and part, perform the following operation on s until all occurrences of the substring part are removed:
• Find the leftmost occurrence of the substring part and remove it from s.
Return s after removing all occurrences of part.
A substring is a contiguous sequence of characters in a string.

Example 1:

    Input: s = "daabcbaabcbc", part = "abc"
    Output: "dab"
    Explanation: The following operations are done:
    - s = "daabcbaabcbc", remove "abc" starting at index 2, so s = "dabaabcbc"
    - s = "dabaabcbc", remove "abc" starting at index 4, so s = "dababc"
    - s = "dababc", remove "abc" starting at index 3, so s = "dab".
    Now s has no occurrences of "abc"



Constraints:
• 1 <= s. length <= 1000
• 1 < part. length <= 1000
• s and part consists of lowercase English letters.

"""



class Solution:
    # Brute for
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    
    def removeOccurrencesII(self, s: str, part: str) -> str:

        while part in s:
            part_start_index = s.find(part)

            s = s[:part_start_index] + s[part_start_index + len(part):]

        return s



    def _check_match(self, stack: list, part: str) -> bool:
        # Compare the top 'part_length' elements of the stack with 'part'
        part_length = len(part)

        return "".join(stack[-part_length:]) == part

    # Time Complexity: O(n * m)
    # Space Complexity: O(n + m)
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = []
        m = len(part) - 1

        for ch in s:
            stack.append(ch)


            if len(stack) >= len(part) and self._check_match(stack, part):
                for _ in range(len(part)):
                    stack.pop()

        return "".join(stack)



        



        print(s)

s = "ixcupqoixcupqokevnpokevnpoknqywmlhevgc"
part = "ixcupqokevnpo"
#    0123456789
s = "daabcbaabcbc"
part = "abc"



solution = Solution()

print("res:", solution.removeOccurrences(s, part))
