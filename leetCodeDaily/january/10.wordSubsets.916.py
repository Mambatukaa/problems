"""


916. Word Subsets

You are given two string arrays words1 and words2.
    A string b is a subset of string a if every letter in b occurs in a including multiplicity.

• For example, "wrr" is a subset of "warrior" but is not a subset of "world".
    A string a from words1 is universal if for every string b in words2, b is a subset of a.

    Return an array of all the universal strings in words1. You may return the answer in any order.


Constraints:

    • 1 < words1.length, words2.length <= 10^4
    • 1 < words1[i].length, words2[i].length <= 10
    • words1[i] and words2[i] consist only of lowercase English letters.
    • All the strings of words1 are unique.

Example 3:
    Input: words1 = ["acaac", "cccbb", "aacbb", "caacc", "bcbbb"], words2 = ["c", "cc", "b"]
    Output: ["cccbb" ]
"""

# Time Complexity: O(A+B), where A and B is the total amount of information in words1 and words2 respectively.
# Space Complexity: O(A.length+B.length).
#
# Reduce to single word in b
# LeetCode solution

Space Complexity: O(A.length+B.length).
def wordSubsets(words1, words2):
    def countLetters(word):
        res = [0] * 26

        for ch in word:
            res[ord(ch) - ord("a")] += 1

        return res

    words2Max = [0] * 26

    for word in words2:
        for i, c in enumerate(countLetters(word)):
            words2Max[i] = max(words2Max[i], c)

    ans = []

    for word in words1:
        if all( x >= y for x, y in zip(countLetters(word), words2Max)):
            ans.append(word)

    

    return ans



    
words1 = ["acaac", "cccbb", "aacbb", "caacc", "bcbbb"]

words2 = ["c", "cc", "b"]

print("res:", wordSubsets(words1, words2))
