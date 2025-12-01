""""





"""


# Time Complexity: O(2n)
# Space Complexity: O(k) k is the size of the set
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()

        res = 0

        l = 0

        for r in range(len(s)):
            curr = s[r]

            while curr in seen:
                seen.remove(s[l])
                l += 1

            res = max(res, r - l + 1)

            seen.add(curr)

        return res



# Optimized
# Time Complexity: O(n)
# Space Complexity: O(k) k is the size of the set
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        # charToNextIndex stores the index after current character
        charToNextIndex = {}

        i = 0
        # try to extend the range [i, j]
        for j in range(n):
            if s[j] in charToNextIndex:
                i = max(charToNextIndex[s[j]], i)

            ans = max(ans, j - i + 1)
            charToNextIndex[s[j]] = j + 1

        return ans
