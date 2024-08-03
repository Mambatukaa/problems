


# TIME LIMIT EXCEEDED
# Time complexity: O(n * m * k) k = length of words
# Space complexity: O(n * m * k)
def wordSearchII(board, words):
  m = len(board)
  n = len(board[0])


  seen = set()

  def dfs(r, c, i, word):
    if i == len(word):
      return True

    if (r < 0 or 
        c < 0 or
        r == m or
        c == n or
        (r, c) in seen or
        board[r][c] != word[i]
        ):
      return False

    seen.add((r,c))

    res = (dfs(r + 1, c, i + 1, word) or
           dfs(r - 1, c, i + 1, word) or
           dfs(r, c + 1, i + 1, word) or
           dfs(r, c - 1, i + 1, word)
           )

    seen.remove((r,c))

    return res



  res = set()

  for row in range(m):
    for col in range(n):

      for word in words:
        seen = set()

        if board[row][col] == word[0] and dfs(row, col, 0, word):
          res.add(word)

  return list(res)

board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]] 
words = ["oath","pea","eat","rain"]


print("res:", wordSearchII(board, words))

"""


Given an m x n board of characters and a list of strings words, return all words on the board.

Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically
neighboring. The same letter cell may not be used more than once in a word.



Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["eat","oath"]



[
["o","a","b","n"],
["o","t","a","e"],
["a","h","k","r"],
["a","f","l","v"]]





"""
