"""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

 

Example 1:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true
Example 2:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:


Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false
 

Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.
 

Follow up: Could you use search pruning to make your solution faster with a larger board?
"""


class Solution:
    def exist(self, board, word: str) -> bool:

        # find the first letter of the word
        # start bfs or dfs from that letter
        # visit neighbors to search actual word
        # if the neighbor character is not equal to current don't continue


        visited = set()
        def dfs(row, col, idx):
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or (row, col) in visited or board[row][col] != word[idx]:
                return False

            visited.add((row, col))

            if idx == len(word) - 1:
                return True

            res = (
                dfs(row + 1, col, idx + 1) or
                dfs(row - 1, col, idx + 1) or
                dfs(row, col + 1, idx + 1) or
                dfs(row, col - 1, idx + 1)
            )

            visited.remove((row, col))

            return res

        ROWS = len(board)
        COLS = len(board[0])

        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == word[0]:
                    visited = set()

                    if dfs(row, col, 0):
                        return True

        return False

        
        
solution = Solution()
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]

word = "ABCCED"
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"
print("res:", solution.exist(board, word))
