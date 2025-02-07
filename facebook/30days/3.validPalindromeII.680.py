""""


Given a string s, return true if the s can be palindrome after deleting at most one character from it.

Example 1:
    Input: s = "aba"
    Output: true

Example 2:
    Input: s = "abca"
    Output: true
    Explanation: You could delete the character 'c'

Example 3:
    Input: s = "abc"
    Output: false


Constraints:
• 1 < s.length <= 10^5
• s consists of lowercase English letters.

"""


class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def validPalindrome(self, s: str) -> bool:
        def rec(l, r, chance):
            if l >= r:
                return True

            if s[l] != s[r]:
                if not chance:
                    return False
                
                return rec(l + 1, r, 0) or rec(l, r - 1, 0)

            return rec(l + 1, r - 1, chance)


        return rec(0, len(s) - 1, 1)

    # Time Complexity: O(n)
    # Space Complexity: O(1)
    def validPalindromeII(self, s: str) -> bool:
        def isPalindrome(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True


        l = 0
        r = len(s) - 1

        while l < r:

            if s[l] != s[r]:
                # remove both sides
                return isPalindrome(l + 1, r) or isPalindrome(l, r - 1)

            l += 1
            r -= 1
        return True
            


solution = Solution()

s = "bcaac"
print("res:", solution.validPalindrome(s))
print("res:", solution.validPalindromeII(s))






