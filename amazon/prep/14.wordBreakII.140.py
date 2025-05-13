""""
Given a string s and a dictionary of strings wordDict, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

 

Example 1:

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]
Example 2:

Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []
 

Constraints:

1 <= s.length <= 20
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 10
s and wordDict[i] consist of only lowercase English letters.
All the strings of wordDict are unique.
Input is generated in a way that the length of the answer doesn't exceed 105.
















"""


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        # iterate through words and create every possible to paths to build S
        # if S has built successfully add current path to the answer
        # backtracking


        res = []

        memo = {}

        def dp(i, curr):
            if i >= len(s):
                res.append(" ".join(curr))
                return

            for word in wordDict:
                n = len(word)
                part = s[i:i + n]
                curr.append(part)

                if part == word:
                    dp(i + n, curr)

                curr.pop()

        dp(0, []) 
        return res




class Solution:
    def wordBreak(self, s: str, wordDict):
        wordSet = set(wordDict)
        memo = {}


        # memo remaining string

        def dfs(remaining):
            if remaining in memo:
                return memo[remaining]

            if not remaining:
                return [""]

            res = []
            for i in range(1, len(remaining) + 1):
                curr_word = remaining[:i]

                if curr_word in wordSet:
                    for next_word in dfs(remaining[i:]):

                        res.append(curr_word + (" " if next_word else "") + next_word)

            memo[remaining] = res

            return memo[remaining]

        return dfs(s)






s = "catsanddog"

wordDict = ["cat","cats","and","sand","dog"]

solution = Solution()

print("res:", solution.wordBreak(s, wordDict))
