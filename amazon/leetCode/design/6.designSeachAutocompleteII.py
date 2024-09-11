from collections import defaultdict
from heapq import nsmallest

"""


Python's heapq module provides functions nsmallest and nlargest.
They take lists as input and return the n best elements. 
When performed on a list of length m, these methods have a 
time complexity of O(m+n⋅logm). We have n = 3 here,
so the time complexity is O(m+logm)=O(m).


#Given n as the length of sentences, k as the average 
# length of all sentences, and m as the number of times 
# input is called,


"""

# Time Complexity: O(n * k + m * (n + m / k))
# Space Complexity: O(k * (n * k + m))
class TrieNode:
    def __init__(self):
      self.children = {}
      self.sentences = defaultdict(int) 

class AutocompleteSystem:
    def __init__(self, sentences, times):
      self.root = TrieNode()

      for sentence, count in zip(sentences, times):
        self.addToTrie(sentence, count)

      self.currSentence = []
      self.currNode = self.root

      # dummy
      self.deadNode = TrieNode()

        
    def input(self, c):
      
      # NOTE finish it and add currSentence to the trie and clear currentSentence
      if c == "#":
        currSentence = "".join(self.currSentence)

        self.addToTrie(currSentence, 1)
        self.currSentence = []
        self.currNode = self.root

        print("Input has finished")

      # NOTE collect character to the currentSentence
      self.currSentence.append(c)

      # NOTE if currentNode has not c
      if c not in self.currNode.children:
        # The future input we can't find a word
        self.currNode = self.deadNode

        return []




      # NOTE if trie has c
      self.currNode = self.currNode.children[c]

      items = [(val, key) for key, val in self.currNode.sentences.items()]

      ans = nsmallest(3, items)


      return [item[1] for item in ans]

    def addToTrie(self, sentence, count):
      curr = self.root

      for c in sentence:
        if not c in curr.children:
          curr.children[c] = TrieNode()
        curr = curr.children[c]
        curr.sentences[sentence] -= count
      
      print(f"Successfully added {sentence} to the trie")

autocompleteSystem = AutocompleteSystem(["i love you", "island", "iroman", "i love leetcode"], [5, 3, 2, 2])

print(autocompleteSystem.input("i"))
print(autocompleteSystem.input(" "))
print(autocompleteSystem.input("a"))

print(autocompleteSystem.input("#"))


# STORED WORDS
print(autocompleteSystem.root.children["i"].sentences)


