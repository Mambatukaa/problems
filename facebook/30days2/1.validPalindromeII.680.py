"""
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
class Solution:
    # 12 minutes
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(left, right, skipped):
            if left >= right:
                return True

            if skipped and s[left] != s[right]:
                return False

            if s[left] == s[right]:
                return isPalindrome(left + 1, right - 1, skipped)
            
            return isPalindrome(left, right - 1, True) or isPalindrome(left + 1, right, True)

        return isPalindrome(0, len(s) - 1, False)


# Optimal
    # Time Complexity: O(n)
    # Space Complexity: O(1)
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
        
"""

deleting at most one character from it.

example 1:
    s = "aba"
    o: True

example 2:
    s = "abca" ---> delete b or c
    o: True



Palindrome reads the same backward as forward

aba VALID
abca VALID

left pointer
right pointer

 l r
abbca -- c --> abba
    skip left:
        l += 1

          lr
        axbca
    skip right:
        r -= 1
         lr
        abbxa

if the l == r:
    l += 1
    r -= 1
    continue

def isPalindrome(word, l, r):
    # check is the word valid or not



abbca

"""
