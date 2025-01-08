"""


Example 1:
    Input: words = ["a", "aba", "ababa", "aa"]|
    Output: 4

Explanation: In this example, the counted index pairs are:
i = 0 and j = 1 because isPrefixAndSuffix("a", "aba") is true.
i = 0 and j = 2 because isPrefixAndSuffix("a", "ababa") is true.
i = 0 and j = 3 because isPrefixAndSuffix("a", "aa") is true.
i = 1 and j = 2 because isPrefixAndSuffix("aba", "ababa") is true.
Therefore, the answer is 4.

"""



# Brute Force
# Time Complexity: O(n^2 * m) n is words lenght m is the string length... m - A prefix check and A suffix check
# Space Complexity: O(n^2 * m^2)
def countPrefixSuffixPairs(words):
    res = 0

    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            str1 = words[i]
            str2 = words[j]

            if len(str1) > len(str2):
                continue

            if str2.startswith(str1) and str2.endswith(str1):
                res += 1

    return res

words = ["a", "aba", "ababa", "aa"]

print("res:", countPrefixSuffixPairs(words))
