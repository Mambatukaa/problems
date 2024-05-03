class TrieNode:
  def __init__(self):
    self.children = {}
    self.endOfString = False

class WordDictionary:
    def __init__(self):
      self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
      current = self.root

      for i in range(len(word)):
        ch = word[i]

        node = current.children.get(ch)

        if not node:
          node = TrieNode()
        
        current.children[ch] = node
        current = node
      
      current.endOfString = True
      print("Successfully added word:", word)
        

    def search(self, word: str) -> bool:

      def helper(root, word, idx):
        if len(word) <= idx:
          return root.endOfString

        ch = word[idx]

        if ch == ".":
          children = root.children

          for child in children:
            res = helper(children[child], word, idx + 1)

            if res:
                return True

        node = root.children.get(ch)

        if not node:
          return False

        return helper(node, word, idx + 1)

      return helper(self.root, word, 0)

obj = WordDictionary()

obj.addWord("at")
obj.addWord("and")
obj.addWord("an")
obj.addWord("add")

obj.search("a")
obj.search(".at")

obj.addWord("bat")

obj.search(".at")
obj.search("an.")
obj.search("a.d.")
obj.search("b.")
obj.search("a.d")
obj.search(".")


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)



"""

Implement Trie DS and 

"""
