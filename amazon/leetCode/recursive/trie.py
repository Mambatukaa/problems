from collections import defaultdict

class TrieNode:
  def __init__(self):
    self.children = defaultdict()
    self.endOfString = False


class Trie:
  def __init__(self):
    self.root = TrieNode()
    print("************************ The Trie has been created. ************************")

  def insert(self, word):
    current = self.root

    for ch in word:
      node = current.children.get(ch)

      if not node:
        node = TrieNode()
        current.children[ch] = node

      current = node

    current.endOfString = True

  def search(self, word):
    current = self.root

    for ch in word:
      node = current.children.get(ch)

      if not node:
        return False
      
      current = node

    return current.endOfString

  def delete(self, word):
    print(word)

trie = Trie()

trie.insert("APP")
trie.insert("API")
trie.insert("APIS")

print("Search APP", trie.search("APP"))
print("Search API", trie.search("API"))
print("Search APIS", trie.search("APIS"))
print("Search APISS", trie.search("APISS"))


