# Use Set to track duplication
# Time Complexity: O(n * m * 4^n)
# Space Complexity: O(n * m * 4^n)
# 1 hour 23 minutes
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

      # row length
      m = len(board)

      # column length
      n = len(board[0])


      #               TOP    BOTTOM   RIGHT   LEFT
      DIRECTIONS = [[-1, 0], [1, 0], [0, 1], [0, -1]]

      def isValid(row, col, curr):
        return row >= 0 and row < m and col >= 0 and col < n and word.startswith(curr + board[row][col]) and not seen.get('%d:%d' % (row, col))

      def dfs(row, col, curr, seen):
        curr += board[row][col]

        

        if curr == word:
          return True

        for [x, y] in DIRECTIONS:
          newRow = row + x
          newCol = col + y

          if isValid(newRow, newCol, curr):
            # row: column, 0:1
            seen['%d:%d' % (newRow, newCol)] = True
            
            if dfs(newRow, newCol, curr, seen):
              return True

            del seen['%d:%d' % (newRow, newCol)]

      # Find the starting point
      for row in range(m):
        
        for col in range(n):
          seen = {}
          seen["%d:%d" % (row, col)] = True

          # Starting point
          if board[row][col] == word[0] and dfs(row, col, "", seen):
            return True

      return False
            




"""

4 DIRECTIONS

TOP
BOTTOM
RIGHT
LEFT

2D ARRAY (row, column)


1. Find first letter from board. STARTING POINT.
2. Start to search words from starting point. To search words build to go every possible directions.
  Every time build new word check the new word is valid or not
    If word is not valid remove and try with other directions
    If word is valid add letter to the new word and repeat
    Once newWord == word 
      return True
  
3. Do the above algorithm until board reaches the end. 

  Helper functions
  * Check duplication
      Set or array
  * Check validation
      Check the range is valid or not




"""


# Use Array to check duplication
# Time Complexity: O(n * 4^n)
# Space Complexity: O(n * 4^n)
# Check old solution

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

      # row length
      m = len(board)

      # column length
      n = len(board[0])


      #               TOP    BOTTOM   RIGHT   LEFT
      DIRECTIONS = [[-1, 0], [1, 0], [0, 1], [0, -1]]

      def isValid(row, col, seen):
        return row >= 0 and row < m and col >= 0 and col < n and not seen[row][col]

      def dfs(row, col, i, seen):
        if i == len(word):
          return True

        for [x, y] in DIRECTIONS:
          newRow = row + x
          newCol = col + y

          if isValid(newRow, newCol, seen) and board[newRow][newCol] == word[i]:
            # row: column, 0:1
            seen[newRow][newCol] = True

            if dfs(newRow, newCol, i + 1, seen):
              return True

            seen[newRow][newCol] = False

      # Find the starting point
      for row in range(m):
        
        for col in range(n):

          # fill map 
          seen = [[False for j in range(n)] for i in range(m)]

          seen[row][col] = True

          # Starting point
          if board[row][col] == word[0] and dfs(row, col, 1, seen):
            return True

      return False


# Neetcode solution

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
      ROWS, COLS = len(board), len(board[0])
      path = set()

      def dfs(r, c, i):
        if i == len(word):
          return True

        if (r < 0 or r >= ROWS or 
            c < 0 or c >= COLS or 
            word[i] != board[r][c] or 
            (r, c) in path):
            return False

        path.add((r,c))

        res = (dfs(r + 1, c, i + 1) or
               dfs(r - 1, c, i + 1) or
               dfs(r, c + 1, i + 1) or
               dfs(r, c - 1, i + 1))

        path.remove((r,c))

        return res

      # Find the starting point
      for row in range(ROWS):
        for col in range(COLS):
          if board[row][col] == word[0] and dfs(row, col, 0):
            return True

      return False

