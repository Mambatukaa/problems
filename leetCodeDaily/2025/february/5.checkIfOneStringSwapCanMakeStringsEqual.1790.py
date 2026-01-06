""""


You are given two strings s1 and s2 of equal length. A string swap is an operation where you choose two
indices in a string (not necessarily different) and swap the characters at these indices.
Return true if it is possible to make both strings equal by performing at most one string swap on exactly one
of the strings. Otherwise, return false.

Example 1:

    Input: s1 = "bank", s2 = "kanb"
    Output: true
    Explanation: For example, swap the first character with the last character of s2 to
    make "bank"

Example 2:

    Input: s1 = "attack", s2 = "defend"
    Output: false
    Explanation: It is impossible to make them equal with one string swap.


Constraints:
• 1 < s1. length, s2. length < 100
• s1. length == s2. length
• s1 and s2 consist of only lowercase English letters.
"""


class Solution:
    # Time Complexity: O(n)
    # Space Complexity: O(1) 26 letters
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True

        s1Count = [0] * 26
        s2Count = [0] * 26

        diff = 0

        for i in range(len(s1)):
            s1Char = s1[i]
            s2Char = s2[i]

            if s1Char != s2Char:
                diff += 1

                if diff > 2:
                    return False

            s1Count[ord("a") - ord(s1Char)] += 1
            s2Count[ord("a") - ord(s2Char)] += 1

        return s1Count == s2Count

    # Time Complexity: O(n)
    # Space Complexity: O(1) NO MAP
    def areAlmostEqualII(self, s1: str, s2: str) -> bool:
        firstIdxDiff = 0
        secondIdxDiff = 0

        numDiffs = 0

        for i in range(len(s1)):
            s1Char = s1[i]
            s2Char = s2[i]

            if s1Char != s2Char:
                numDiffs += 1

                if numDiffs > 2:
                    return False
                
                if numDiffs == 1:
                    firstIdxDiff = i
                else:
                    secondIdxDiff = i

        return s1[firstIdxDiff] == s2[secondIdxDiff] and fs1[secondIdxDiff] == s2[firstIdxDiff]
