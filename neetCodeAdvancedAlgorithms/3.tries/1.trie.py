class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        node = self.root

        for letter in word:
            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]

        node.isWord = True

    def search(self, word):
        node = self.root

        for letter in word:
            if letter not in node.children:
                return False
            
            node = node.children[letter]

        return node.isWord

    def startsWith(self, prefix):
        node = self.root

        for c in prefix:
            if c not in node.children:
                return False
            
            node = node.children[c]

        return True



trie = Trie()

trie.addWord("Hello"))
print(trie.search("Hello"))


