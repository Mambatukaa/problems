"""

Given a strings, find the length of the longest substring without repeating characters.

Example 1:
    Input: s = "abcabcbb"
    Output: 3
    Explanation: The answer is "abc", with the length of 3.

Example 2:
    Input: s = "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.

Example 3:
    Input: s = "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3.
        Notice that the answer must be a substring, "pwke" is a subsequence and not a
        substring.


"""


# Sliding window
# Time Complexity: O(n)
# Space Complexity: O(n)
# Also you can use array instead of set
def longest(s):
    res = 0
    seen = set()

    l = 0
    r = 0

    while r < len(s):

        # increase the left pointer until remove the s[r] from seen
        while s[r] in seen:
            seen.remove(s[l])
            l += 1

        seen.add(s[r])
        res = max(res, r - l + 1)

        r += 1

    return res

#     l
#        r
#    01234567
s = "abcabcbb"

print("res:", longest(s))
