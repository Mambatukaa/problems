class Node:
    def __init__(self):
        self.children = [None] * 26
        self.frequency = 0



class Trie:
    def __init__(self):
        self.root = Node()
    

    def _insert(self, word):
        currNode = self.root

        for ch in word:
            idx = ord(ch) - ord("a")

            if not currNode.children[idx]:
                currNode.children[idx] = Node()

            currNode = currNode.children[idx]
            currNode.frequency += 1

        print("You successfully added a word")

    def _countFreq(self, word):
        currNode = self.root

        for ch in word:
            idx = ord(ch) - ord("a")

            if not currNode.children[idx]:
                return 0
            
            currNode = currNode.children[idx]

        return currNode.frequency



class Solution:
    # Time Complexity: O(n * m) The outer loop iterates through each string in the array words, which takes O(n) operations. For each string, the startsWith method needs to compare characters until it reaches the end of the prefix or finds a mismatch. In the worst case, this comparison takes O(m) operations.
    # Space Complexity: O(n * m)
    # Built-in Methods
    def prefixCount(self, words, pref: str) -> int:
       res = 0 

       for word in words:
        if word.startswith(pref):
            res += 1
            
       return res

    # Trie
    # Time Complexity: O(n * l + m) l is the maximum length of any string m is the length of pref
    # Space Complexity: O(n * l) n words of maximum length is l
    def prefixCountII(self, words, pref):
        trie = Trie()

        for word in words:
            trie._insert(word)

        return trie._countFreq(pref)


words = ["pay","attention","practice","attend"] 
pref = "at"

solution = Solution()
print("res:", solution.prefixCountII(words, pref))


