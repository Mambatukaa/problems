class Node:
    def __init__(self):
        self.children = {}


class Trie:
    def __init__(self):
        self.root = Node()

    # Insert a word into the Trie
    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = Node()

            node = node.children[c]

    # Check if the Trie contains a given prefix
    def starts_with(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            if c not in node.children:
                return False
            node = node.children[c]
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
