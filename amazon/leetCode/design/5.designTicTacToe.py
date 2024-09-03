
# Naive approach
# Time Complexity: O(n^2)
# Space Complexity: O(n)
class TicTacToe:

  # n is a size of the board
  def __init__(self, n):
    self._n = n
    self._board = [[None for _ in range(n)] for _ in range(n)]

    print("Successfully created a board size", n)

  def checkWin(self, row, col, player):
    counter = 0

    # check horizontal
    # check only current row
    for c in range(self._n):
      if self._board[row][c] == player:
        counter += 1

        if counter == self._n:
          return True
      else:
        break


    counter = 0
    # check vertical
    # check only current column
    for r in range(self._n):
      if self._board[r][col] == player:
        counter += 1

        if counter == self._n:
          return True
      else:
        break

    if row == col:
      counter = 0
      # check diagonal
      for r in range(self._n):
        c = r
        if self._board[r][c] == player:
          counter += 1

          if counter == self._n:
            return True
        else:
          break

      counter = 0
      # check anti diagonal

      for r in range(self._n):
        c = self._n - 1 - r

        if self._board[r][c] == player:
          counter += 1

          if counter == self._n:
            return True
        else:
          break

    return False

  def move(self, row, col, player):
    mark = "X" if player == 1 else "O"
    
    self._board[row][col] = mark

    if self.checkWin(row, col, mark):
      return player
    
    return 0

  def printBoard(self):

    print("Board: ---------------------------------------------")
    for i in range(self._n):
      print(self._board[i])

    print("---------------------------------------------")

ticTacToe = TicTacToe(2)

ticTacToe.printBoard()


print(ticTacToe.move(0, 1, 2))
print(ticTacToe.move(1, 0, 1))
print(ticTacToe.move(1, 1, 2))

ticTacToe.printBoard()

"""

Constraints:

  • 2 <= n <= 100
  • player is 1 or 2.
  • 0 <= row, col < n
  • (row, col) are unique for each different call to move.
  • At most n? calls will be made to move .

Follow-up: Could you do better than 0(n2) per move () operation?


"""
