""""

A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The lengths should not
have leading zeros.
For example, a string such as "substitution" could be abbreviated as (but not limited to):
• "s10n" ("s ubstitutio n")
• "sub4u4" ("sub stit u tion")
• "12" ("substitution" )
• "su3ilu2on" ("su bst i t u ti on")
• "substitution" (no substrings replaced)
The following are not valid abbreviations:
• "s55n" ("s ubsti tution", the replaced substrings are adjacent)
• "s010n" (has leading zeros)
• "substitution" (replaces an empty substring)
Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.
A substring is a contiguous non-empty sequence of characters within a string.

Example 1:
Input: word = "internationalization", abbr = "i12iz4n"
Output: true
Explanation: The word "internationalization" can be abbreviated as "i12iz4n" ("i nternational iz atio n")




Constraints:
• 1 <= word.length <= 20)
• word consists of only lowercase English letters.
• 1 <= abbr.length <= 10
• abbr consists of lowercase English letters and digits.
• All the integers in abbr will fit in a 32-bit integer.


"""


class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        n = len(word)
        m = len(abbr)

        i = 0
        j = 0
        while i < m and j < n:
            if abbr[i] == word[j]:
                i += 1
                j += 1

                continue

            if not abbr[i].isdigit:
                return False

            steps = int(abbr[i])

            if i < m - 1 and abbr[i + 1].isdigit():
                steps = steps * 10 + int(abbr[i + 1])
                i += 1

            j += steps
            i += 1

            if i < m and j < n and abbr[i] != word[j]:
                return False

        return j == n and i == m



word = "internationalization"
abbr = "i12iz4n"

word = "aaaaaa"
abbr = "6"

word = "internationalization"
abbr = "i5a11o1"

word = "hi"
abbr = "hi1"

solution = Solution()

print("res:", solution.validWordAbbreviation(word, abbr))
