"""
Given a string s, return the number of unique palindromes of length three that are a subsequence of s.
Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.
A palindrome is a string that reads the same forwards and backwards.
A subsequence of a string is a new string generated from the original string with some characters (can be
none) deleted without changing the relative order of the remaining characters.

• For example, "ace" is a subsequence of "abcde" .


Example 1:
Input: s = "aabca"
Output: 3
Explanation: The 3 palindromic subsequences of length 3 are:
- "aba" (subsequence of "aabca")
- "aaa" (subsequence of "aabca")
- "aca" (subsequence of "aabca")



1. Find the pair values using two pointers (left, right)
2.

"""

from collections import Counter


# TIME LIMIT EXCEEDED
# Time complexity: O(n^2)
# Space Complexity: O(n)
# Brute Force
def countPalindromicSubsequence(s):
    res = set()

    n = len(s)
    l = 0
    r = n - 1

    while l < n:
        temp = r

        while s[l] != s[temp]:
            temp -= 1

        for i in range(l + 1, temp):
            res.add(s[l] + s[i] + s[temp])

        l += 1

    return len(res)

# Time complexity: O(n)
# Space Complexity: O(n)
# NeetCode
def countPalindromicSubsequenceII(s):
    left = set()
    rightMap = Counter(s)

    res = set()

    for m in s:
        rightMap[m] -= 1

        for item in left:
            if rightMap[item] >= 1:
                res.add(item + m)

        left.add(m)

        if rightMap[m] == 0:
            del rightMap[m]
            left.remove(m)

    return len(res)

#    0123456
s = "aabcbca"

print("res:", countPalindromicSubsequenceII(s))
