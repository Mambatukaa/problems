class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
        print("You successfully created a trie")

    # TC: O(M) M = characters 
    # SC: O(M)
    def insert(self, word):
        current = self.root

        for i in range(len(word)):
            ch = word[i]
            
            node = current.children.get(ch)

            if not node:
                node = TrieNode()
                current.children[ch] = node

            current = node

        current.endOfString = True

        print("Successfully inserted the value")
    
    def search(self, word):
        current = self.root

        for i in range(len(word)):
            ch = word[i]
            
            node = current.children.get(ch)

            if not node:
                return False

            current = node

        return current.endOfString


trie = Trie()

trie.insert("APP")
trie.insert("API")
print(trie.search("A"))
print(trie.search("APP"))
print(trie.search("APPP"))
print(trie.search(".PI"))

