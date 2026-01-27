""""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

 

Example 1:

Input: s1 = "ab", s2 = "eidbaooo"
Output: true
Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

Input: s1 = "ab", s2 = "eidboaoo"
Output: false
 

Constraints:

1 <= s1.length, s2.length <= 104
s1 and s2 consist of lowercase English letters.
"""

""""




TC: O(l2) 
SC: O(1)
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            return False
        
        s1_char_freq = [0] * 26
        s2_window_char_freq = [0] * 26

        for index in range(len(s1)):
            s1_char_freq[ord(s1[index]) - ord("a")] += 1
            s2_window_char_freq[ord(s2[index]) - ord("a")] += 1

        if s1_char_freq == s2_window_char_freq:
            return True

        for index in range(len(s2) - len(s1)):
            s2_window_char_freq[ord(s2[index]) - ord('a')] -= 1
            s2_window_char_freq[ord(s2[index + len(s1)]) - ord('a')] += 1
        
            if s1_char_freq == s2_window_char_freq:
                return True

        return False


        
