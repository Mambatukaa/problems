

# DFS and BFS

class Solution:
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
 ["a","e","d"],
 ["a","f","g"]]

words = ["abcdefg","gfedcbaaa","eaabcdgfa","befa","dgc","ade"]


solution = Solution()

print("res:", solution.wordSearch(board, words))
