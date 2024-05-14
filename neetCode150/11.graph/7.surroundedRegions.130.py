# Time Complexity: O(n * m)
# Space Complexity: O(n * m)
# DFS
# 20 minutes
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        ROWS = len(board)
        COLS = len(board[0])

        def dfs(r, c, seen):
          if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != "O" or (r,c) in seen:
            return

          seen.add((r,c))

          dfs(r + 1, c, seen)
          dfs(r - 1, c, seen)
          dfs(r, c + 1, seen)
          dfs(r, c - 1, seen)

        seen = set()
        
        # top to bottom
        for r in range(ROWS):
          dfs(r, 0, seen)
          dfs(r, COLS - 1, seen)

        # left to right
        for c in range(COLS):
          dfs(0, c, seen)
          dfs(ROWS - 1, c, seen)


        for r in range(ROWS):
          for c in range(COLS):
            if board[r][c] == "O" and (r,c) not in seen:
              board[r][c] = "X"
        

# NEETCODE
# NO SET

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        ROWS = len(board)
        COLS = len(board[0])

        def dfs(r, c):
          if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != "O":
            return

          board[r][c] = "T"

          dfs(r + 1, c)
          dfs(r - 1, c)
          dfs(r, c + 1)
          dfs(r, c - 1)

        # top to bottom
        for r in range(ROWS):
          dfs(r, 0)
          dfs(r, COLS - 1)

        # left to right
        for c in range(COLS):
          dfs(0, c)
          dfs(ROWS - 1, c)

        for r in range(ROWS):
          for c in range(COLS):
            if board[r][c] == "O":
              board[r][c] = "X"
            elif board[r][c] == "T":
              board[r][c] = "O"

        


"""


START FROM 
  TOP
  BOTTOM
  LEFT
  RIGHT

if find 0 start to find neighbor 0's add add to the set


"""
