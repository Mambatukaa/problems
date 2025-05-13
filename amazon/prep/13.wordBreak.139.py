""""
Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "leetcode", wordDict = ["leet","code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple","pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: false
 

Constraints:

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
"""

class Solution:
    # Backtracking with memo
    # Top down DP
    def wordBreak(self, s: str, wordDict) -> bool:
        memo = {}
        def backtracking(i, curr):
            if i in memo:
                return False
            if i >= len(s):
                return True
            
            for word in wordDict:
                n = len(word)

                if curr[:n] == word:
                    if backtracking(i + n, curr[n:]):
                        return True

            memo[i] = False

            return memo[i]


        return backtracking(0, s)

    def wordBreak(self, s: str, wordDict) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[n] = True

        for i in range(n - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= n and s[i : i + len(w)] == w:
                    dp[i] = dp[i + len(w)]

                    if dp[i]:
                        break

        return dp[0]










class TrieNode:
    def __init__(self):
        self.is_word = False
        self.children = {}


class Solution:
    def wordBreak(self, s: str, wordDict) -> bool:
        root = TrieNode()
        for word in wordDict:
            curr = root
            for c in word:
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]

            curr.is_word = True

        dp = [False] * len(s)

        for i in range(len(s)):

            if i == 0 or dp[i - 1]:

                curr = root

                for j in range(i, len(s)):
                    c = s[j]

                    if c not in curr.children:
                        # No words exist
                        break

                    curr = curr.children[c]
                    if curr.is_word:
                        dp[j] = True

        return dp[-1]

        
s = "leetcode"
wordDict = ["leet","code"]


solution = Solution()
print("res:", solution.wordBreak(s, wordDict))











print("leetcode"[0:4])
print("leetcode"[4:9])
