from collections import defaultdict

class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.endOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for ch in word:
            node = node.children[ch]

        node.endOfWord = True

        print("Word Successfully added", word)

    def search(self, word):
        node = self.root

        for ch in word:
            if not node:
                return False

            node = node.children[ch]

        print(word, "found:", node.endOfWord);

        return node.endOfWord


# DFS and BFS

class Solution:
    # Time Complexity: Time complexity: O(M(4*3^L−1 )), where M is the number of cells in the board and L is the maximum length of words.)
    # Space Complexity: O(n) n = total numbers of letters in the dictionary
    # SEARCH FROM TRIE
    def wordSearchII(self, board, words):
        trie = Trie()

        for word in words:
            trie.insert(word)

        ROWS = len(board)
        COLS = len(board[0])

        res = set()
        seen = set()

        def dfs(r, c, node, curr):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in seen or board[r][c] not in node.children:
                return 


            node = node.children[board[r][c]]
            curr += board[r][c]

            if node.endOfWord:
                res.add(curr)

            seen.add((r,c))

            dfs(r + 1, c, node, curr)
            dfs(r - 1, c, node, curr)
            dfs(r, c + 1, node, curr)
            dfs(r, c - 1, node, curr)

            seen.remove((r,c))

        for row in range(ROWS):
            for col in range(COLS):
                dfs(row, col, trie.root, "")

        return list(res)


    # DFS backtracking
    # Time Complexity: O(k * m * n) k is the words length
    # Space Complexity: O(m * n) 
    # TIME LIMIT EXCEEDED ----------------------------------------------
    def wordSearch(self, board, words):
        self.res = set()

        ROWS = len(board)
        COLS = len(board[0])

        def search(r, c, word, seen, currIdx):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in seen or board[r][c] != word[currIdx]:
                return False

            if currIdx + 1 == len(word):
                return True

            seen.add((r,c))

            res = (search(r + 1, c, word, seen, currIdx + 1) or
                   search(r - 1, c, word, seen, currIdx + 1) or
                   search(r, c + 1, word, seen, currIdx + 1) or
                   search(r, c - 1, word, seen, currIdx + 1))

            seen.remove((r,c))

            return res
                    
        for word in words:
            for r in range(ROWS):
                for c in range(COLS):
                    if board[r][c] == word[0]:
                        seen = set()

                        # Search word
                        if search(r, c, word, seen, 0):
                            self.res.add(word)

        return list(self.res)

board = [
            ["o","a","a","n"],
            ["e","t","a","e"],
            ["i","h","k","r"],
            ["i","f","l","v"]
        ]

words = ["oath", "o", "iflv"]

board = [["o","a","b","n"],
         ["o","t","a","e"],
         ["a","h","k","r"],
         ["a","f","l","v"]]
words = ["oa","oaa"]

board = [["a", "a"]]
words = ["aaa"]

board = [
 ["a","b","c"],
 ]

words = ["abc"]


solution = Solution()

print("res:", solution.wordSearch(board, words))
print("------------------------------------------")
print("res II:", solution.wordSearchII(board, words))
