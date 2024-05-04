class TrieNode:
  def __init__(self):
    self.children = {}
    self.endOfString = False

# Time Complexity: O(M)
# Space Complexity: O(M)
# 1 day
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

      def dfs(idx, root):
        curr = root

        for i in range(idx, len(word)):
            ch = word[i]

            if ch == '.':
                for child in curr.children.values():
                    if dfs(i + 1, child):
                        return True
                return False
            else:
                if ch not in curr.children:
                    return False
                curr = curr.children[ch]

        return curr.endOfString


      return dfs(0, self.root)

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
