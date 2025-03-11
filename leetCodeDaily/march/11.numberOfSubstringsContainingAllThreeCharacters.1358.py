""""

Given a string s consisting only of characters a, b and c.
Return the number of substrings containing at least one occurrence of all these characters a, b and c.

Example 1:
Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the
characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc",
"cab" "cabc" and "abc" (again).
Example 2:
Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the
characters a, b and c are "aaacb" ', "aacb" and "acb"
Example 3:
Input: s = "abc"
Output: 1

Constraints:
• 3 <= s. length <= 5 × 10^4
• s only consists of a, b or c characters.


"""

class Solution:
    # Sliding window
    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        characters_count = {}

        start = end = 0
        res = 0

        while end < n:
            letter = s[end]

            characters_count[letter] = characters_count.get(letter, 0) + 1

            # shrink the window
            while len(characters_count) == 3:
                res += n - end

                start_letter = s[start]
                characters_count[start_letter] -= 1

                if characters_count[start_letter] == 0:
                    del characters_count[start_letter]

                start += 1

            end += 1

        return res

