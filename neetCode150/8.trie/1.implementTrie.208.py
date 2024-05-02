class TrieNode:
  def __init__(self):
    self.children = {}
    self.endOfString = False

# Time Complexity: O(M) // M s length of word
# Time Complexity: O(M)
class Trie:

    def __init__(self):
      self.root = TrieNode()

    def insert(self, word: str) -> None:
      current = self.root

      for i in range(len(word)):
        ch = word[i]
        node = current.children.get(ch)

        if not node:
          node = TrieNode()
        
        current.children[ch] = node
        current = node
      
      current.endOfString = True
        

    def search(self, word: str) -> bool:
      current = self.root

      for i in range(len(word)):
        ch = word[i]
        node = current.children.get(ch)

        if not node:
          return False
        
        current = node
      
      return current.endOfString
        

    def startsWith(self, prefix: str) -> bool:
      current = self.root

      for i in range(len(prefix)):
        ch = prefix[i]

        node = current.children.get(ch)

        if not node:
          return False
        
        current = node
      
      return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
