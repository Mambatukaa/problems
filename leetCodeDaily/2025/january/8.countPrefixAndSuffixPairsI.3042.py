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



class Node:
    def __init__(self):
        self.children = [None] * 26

# Trie        
# Time Complexity: O(n^2 * m) The algorithm involves a nested loop where the outer loop runs n times and the inner loop runs i times for each iteration of the outer loop. For each pair of words, the insert and startsWith operations are performed on the Trie. The insert operation takes O(m) time, and the startsWith operation also takes O(m) time. Therefore, the overall time complexity is O(n 2 ⋅m).
# Space Complexity: O(n * m)
class Trie:
    def __init__(self):
        self.root = Node()

    # Insert a word into the Trie
    def insert(self, word: str) -> None:
        node = self.root

        for c in word:
            idx = ord(c) - ord("a")
            if not node.children[idx]:
                
                node.children[idx] = Node()

            node = node.children[idx]

    # Check if the Trie contains a given prefix
    def starts_with(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            idx = ord(c) - ord("a")
            if not node.children[idx]:
                return False
            node = node.children[idx]
        return True

class Solution:
    def countPrefixSuffixPairs(self, words) -> int:
        n = len(words)
        count = 0

        # Step 1: Iterate over each word
        for i in range(n):
            prefix_trie = Trie()
            suffix_trie = Trie()

            # Step 2: Insert the current word into the prefix Trie
            prefix_trie.insert(words[i])

            # Step 3: Reverse the word and insert it into the suffix Trie
            rev_word = words[i][::-1]
            suffix_trie.insert(rev_word)

            # Step 4: Iterate over all previous words
            for j in range(i):
                # Step 5: Skip words[j] if it is longer than words[i]
                if len(words[j]) > len(words[i]):
                    continue
         
                # Step 6: Extract the prefix and reversed prefix of words[j]
                prefix_word = words[j]
                rev_prefix_word = prefix_word[::-1]

                # Step 7: Check if words[j] is both a prefix and suffix of words[i]
                if prefix_trie.starts_with(prefix_word) and suffix_trie.starts_with(rev_prefix_word):
                    count += 1

        # Step 8: Return the total count of valid pairs
        return count

words = ["pa", "papa", "ma", "mama"]
solution = Solution()

print("res:", solution.countPrefixSuffixPairs(words))

# REVERSE STRING 
# print("abc"[::-1])

