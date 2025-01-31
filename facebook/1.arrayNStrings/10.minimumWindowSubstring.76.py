


"""
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t
(including duplicates) is included in the window. If there is no such substring, return the empty string ""
The testcases will be generated such that the answer is unique.



Example 1:
    Input: s = "ADOBECODEBANC", t = "ABC"|
    Output: "BANC"
    Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.

Example 2:
    Input: s = "a", t = "a"
    Output: "a"
    Explanation: The entire string s is the minimum window.

Example 3:
    Input: s = "a", t = "aa"
    Output: ''
    Explanation: Both 'a's from t must be included in the window.
    Since the largest window of s only has one 'a', return empty string.



Constraints:
• m == s. length
• n == t. length
• 1 <= m, n <= 105)
• s and t consist of uppercase and lowercase English letters.

Follow up: Could you find an algorithm that runs in 0(m + n) time?
"""


from collections import defaultdict, Counter
class Solution:
    # Naive approach
    # Sliding window brute force
    # Time Complexity: O(n * m)
    # Space Complexity: O(n * m)
    def minWindow(self, s: str, t: str) -> str:
        # convert strings to array for better access
        sArr = list(s)
        tArr = list(t)

        tCount = {}

        for ch in tArr:
            if ch not in tCount:
                tCount[ch] = 0

            tCount[ch] += 1


        l = 0
        r = 0

        res = ""

        while r < len(s):
            if s[r] in tCount:
                tCount[s[r]] -= 1

            while all(ch <= 0 for ch in tCount.values()):
                if not res or len(sArr[l:r + 1]) < len(res):
                    res = sArr[l:r+1]

                if s[l] in tCount:
                    tCount[s[l]] += 1

                l += 1

            r += 1

        return ''.join(res)


    # Compare two maps
    def minWindowII(self, s: str, t: str) -> str:
        tCounts = Counter(t)
        sCounts = defaultdict()

        l = 0
        r = 0

        res = ""

        while r < len(s):
            if s[r] not in sCounts:
                sCounts[s[r]] = 0

            sCounts[s[r]] += 1

            while all(sCounts.get(key, 0) >= tCounts[key] for key in tCounts):
                if not res or len(res) > r - l:
                    res = s[l:r + 1]

                sCounts[s[l]] -= 1

                l += 1
            r += 1

        return ''.join(res)


    # optimal solution
    # Time Complexity: O(m + n)
    # Space Complexity: O(m + n)
    def minWindowIII(self, s, t):
        need = {}
        have = {}
        needCount = 0

        for ch in t:
            if ch not in have:
                needCount += 1
                have[ch] = 0
                need[ch] = 0
            
            need[ch] += 1

        haveCount = set()
        l = 0
        r = 0

        res = ""
        # sliding window
        while r < len(s):
            curr = s[r]

            if curr in have:
                have[curr] += 1

                if have[curr] >= need[curr]:
                    haveCount.add(curr)

            # update the answer and shrink the window
            while len(haveCount) == needCount:
                if not res or len(res) > r - l:
                    res = s[l:r + 1]

                curr = s[l]

                if curr in have:

                    have[curr] -= 1

                    if have[curr] < need[curr]:
                        haveCount.remove(curr)

                l += 1

            r += 1

        return res


    # optimal solution
    # Time Complexity: O(m + n)
    # Space Complexity: O(m + n)
    def minWindowIV(self, s, t):
        countT = {}
        window = {}

        for ch in t:
            countT[ch] = 1 + countT.get(ch, 0)


        res = [-1, -1]
        resLength = float('infinity')

        need, have = 0, len(countT)

        l = 0
        r = 0

        while r < len(s):
            curr = s[r]
            window[curr] = 1 + window.get(curr, 0)

            if curr in countT and window[curr] == countT[curr]:
                need += 1

            # shrink the window
            while need == have:
                if resLength > r - l:
                    res = [l, r]
                    resLength = r - l

                if s[l] in countT and window[s[l]] == countT[s[l]]:
                    need -= 1

                window[s[l]] -= 1
                l += 1

            r += 1

        return s[res[0]:res[1] + 1]



s = "bbaa"
t = "aba"

solution = Solution()

print("res:", solution.minWindowIV(s, t))

"""

Have we met the condition


"""
