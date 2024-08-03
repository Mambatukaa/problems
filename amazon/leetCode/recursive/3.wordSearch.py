
# Recursive solution
# Time Complexity: O(m * n)
# Space Complexity: O(m * n)
def wordSearch(board, word):
  m = len(board)
  n = len(board[0])

  seen = set()

  def dfs(r, c, i):
    if i == len(word):
      return True

    if (r < 0 or 
        c < 0 or 
        r >= m or
        c >= n or
        board[r][c] != word[i] or
        (r, c) in seen
        ):
      return False

    seen.add((r, c))

    res = (dfs(r + 1, c, i + 1) or
           dfs(r - 1, c, i + 1) or
           dfs(r, c + 1, i + 1) or
           dfs(r, c - 1, i + 1))

    seen.remove((r, c))

    return res
  
  # Search first letter from wordSearch
  for row in range(m):
    for col in range(n):
      if board[row][col] == word[0]:
        # Search the word
        if dfs(row, col, 0):
          return True

  return False


board = [["a","b"],["c","d"]]
word = "acdb"

board = [
  ["A","B","C","E"],
  ["S","F","C","S"],
  ["A","D","E","E"]
]

word = "ABCCED"

print("res:", wordSearch(board, word))


"""

A B C E
S F C S
A D E E

ABCCED

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.




If word exists return True otherwise return False.


The word can be constructed from letters of sequentially adjacent cells.
  Verically or horizontally neighboring.


board:

A B C E
S F C S
A D E E

word: ABCCED



Solution:

  Starts from first letter and search letter from grid.
    If found start to check neighbors.
      Collect the current constructed values during search.

      Check the current value is valid and continue the step

      If word is found return True

        Otherwise return FALSE


DFS or BFS 





Constraints:

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.


a c 
d b





"""
