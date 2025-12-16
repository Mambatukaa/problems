""""

Given a string s, return true if the s can be palindrome after deleting at most one character from it.

 

Example 1:

Input: s = "aba"
Output: true
Example 2:

Input: s = "abca"
Output: true
Explanation: You could delete the character 'c'.
Example 3:

Input: s = "abc"
Output: false
 

Constraints:

1 <= s.length <= 105
s consists of lowercase English letters.
"""


# TC: O(n)
# SC: O(1)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def isPalindrome(l, r, check):
            while l <= r:
                if s[l] != s[r]:
                    if check:
                        return False
                    return isPalindrome(l + 1, r, True) or isPalindrome(l, r - 1, True)
                l += 1
                r -= 1
            
            return True


        return isPalindrome(0, len(s) - 1, False)


# TC: O(n)
# SC: O(1)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check_palindrome(s, i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            
            return True

        i = 0
        j = len(s) - 1
        while i < j:
            # Found a mismatched pair - try both deletions
            if s[i] != s[j]:
                return check_palindrome(s, i, j - 1) or check_palindrome(s, i + 1, j)
            i += 1
            j -= 1
        
        return True

