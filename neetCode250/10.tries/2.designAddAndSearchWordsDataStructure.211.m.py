""""
Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.
 

Example:

Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True
 

Constraints:

1 <= word.length <= 25
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.
There will be at most 2 dots in word for search queries.
At most 104 calls will be made to addWord and search.
"""


class TrieNode():
    def __init__(self):
        self.children = {}
        self.isWord = False

# Time Complexity: O(n) for addWord and O(m) for search, where n is the length of the word being added and m is the length of the word being searched.
# Space Complexity: O(n) for addWord and O(m) for search, where n
class WordDictionary:
    def __init__(self):
        self.trie = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.trie

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        
        curr.isWord = True

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
    
            return curr.isWord
    
    
        return dfs(0, self.trie)
            


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)



class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = {}

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.trie

        for ch in word:
            if not ch in node:
                node[ch] = {}
            node = node[ch]
        node["$"] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any letter.
        """

        def search_in_node(word, node) -> bool:
            for i, ch in enumerate(word):
                if not ch in node:
                    # if the current character is '.'
                    # check all possible nodes at this level
                    if ch == ".":
                        for x in node:
                            if x != "$" and search_in_node(
                                word[i + 1 :], node[x]
                            ):
                                return True

                    # If no nodes lead to an answer
                    # or the current character != '.'
                    return False

                # If the character is found
                # go down to the next level in trie
                else:
                    node = node[ch]
            return "$" in node

        return search_in_node(word, self.trie)