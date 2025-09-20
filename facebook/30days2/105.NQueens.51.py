# Time Complexity: O(n!)
# Space Complexity: O(n^2)
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:


        res = []
        def backtracking(row, diagonals, anti_diagonals, cols):
            if row == n:
                curr = []
                for row in board:
                    curr.append("".join(row))
                res.append(curr)
                return
            
            for col in range(n):
                curr_diagonal = row - col
                curr_anti_diagonal = row + col

                if col in cols or curr_diagonal in diagonals or curr_anti_diagonal in anti_diagonals:
                    continue

                cols.add(col)
                diagonals.add(curr_diagonal)
                anti_diagonals.add(curr_anti_diagonal)
                board[row][col] = "Q"

                backtracking(row + 1, diagonals, anti_diagonals, cols)

                cols.remove(col)
                diagonals.remove(curr_diagonal)
                anti_diagonals.remove(curr_anti_diagonal)
                board[row][col] = "."

        board = [["."] * n for _ in range(n)]

        backtracking(0, set(), set(), set())

        return res

"""

1. Backtracking check the row, col, diagonal
    Put the queen on the location if it's possible

2. Check every possible ways to location





[
 ".Q..",
 "...Q",
 "Q...",
 "..Q."]

"""
