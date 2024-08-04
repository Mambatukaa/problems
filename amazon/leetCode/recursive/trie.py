from collections import defaultdict

class TrieNode:
  def __init__(self):
    self.children = defaultdict(TrieNode)
    self.endOfString = False


class Trie:
  def __init__(self):
    self.root = TrieNode()
    print("************************ The Trie has been created. ************************")

  def insert(self, word):
    node = self.root

    for ch in word:
      node = node.children[ch]

    node.endOfString = True
    print("The word %s is successfully inserted" % word)

  def search(self, word):
    node = self.root

    for ch in word:
      node = node.children[ch]

      if not node:
        return False

    return node.endOfString

  def delete(self, word):
    print(word)

"""
trie = Trie()

trie.insert("APP")
trie.insert("API")
trie.insert("APIS")

print("Search APP", trie.search("APP"))
print("Search API", trie.search("API"))
print("Search APIS", trie.search("APIS"))
print("Search APISS", trie.search("APISS"))


print(trie.root.children.get("N"))
"""
