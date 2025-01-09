""" 
Given an array of string words, return all strings in words that is a substring of another word. You can return the answer in any order.
A substring is a contiguous sequence of characters within a string

Example 1:
    Input: words = ["mass", "as", "hero", "superhero"]
    Output: ["as", "hero"]

    Explanation: "as" is substring of "mass" and "hero" is substring of "superhero".
"""

# Naive approach
# Brute force
# Time Complexity: O(n^2 * m^2) n is total words m is lenght of string 
# Space Complexity: O(n * m)
def stringMatching(words):
    res = []

    for currWord in words:

        for otherWord in words:
            if currWord == otherWord:
                continue

            if currWord in otherWord:
                res.append(currWord)
                break

    return res


# TRIE
class Solution:

    # Time Complexity: (n * m^2) n - the size of the array, m - length of the longest string
    # Space Complexity: (n * m^2) TRIE
    class Trie:
        def __init__(self):
            self.children = {}
            self.frequency = 0

    def insert(self, word):
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = self.Trie()

            curr = curr.children[ch]
            curr.frequency += 1

    def search(self, word):
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                return False
            
            curr = curr.children[ch]

        return True if curr.frequency > 1 else False

    def stringMatchingII(self, words):
        self.root = self.Trie()
        self.res = []

        # Insert all suffixes of each word into the Trie.
        for word in words:
            for startIndex in range(len(word)):
                # Insert each suffix starting from index start_index.
                self.insert(word[startIndex:])


        # search words
        for word in words:
            if self.search(word):
                self.res.append(word)

        return self.res


words = ["mass", "as", "hero", "superhero"]
solution = Solution()

print("res:", solution.stringMatchingII(words))

