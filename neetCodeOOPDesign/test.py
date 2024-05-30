import enum

class GridPosition(enum.Enum):
  EMPTY = 0
  RED = 1
  YELLOW = 2


class Board:
  def __init__(self, rows, columns):
    self._rows = rows
    self._columns = columns
    self._count = 0

    self._board = None
    self.initBoard(rows, columns)

  def initBoard(self, rows, columns):
    self._board = [[GridPosition.EMPTY for r in range(columns)] for _ in range(rows)]

  def getBoard(self):
    for row in range(self._rows):
      for col in range(self._columns):
        print(self._board[row][col].value, end = " ")
      print('')
  
  def getColumnsCount(self):
    return self._columns

  def placeColor(self, column, color):
    if column >= self._columns or column < 0:
      raise ValueError("Invalid column")
    if color == GridPosition.EMPTY:
      raise ValueError("Invalid color")

    for row in range(self._rows - 1, -1, -1):
      if self._board[row][column] == GridPosition.EMPTY:
        self._board[row][column] = color
        # print("Is player", color.value, "win:", self.checkWin(4, row, column, color))
        return row

    raise ValueError("Column is full!")
  
  def checkWin(self, connectN, row, col, color):
    def check(r, c):
      if self._board[r][c] == color:
        self._count += 1
      else:
        self._count = 0

      if self._count >= connectN:
        return True

    # Check horizontally
    for c in range(self._columns):
      if check(row, c):
        return True

    # reset counter
    self._count = 0

    # Check vertically
    for r in range(self._rows):
      if check(r, col):
        return True
      
    # reset counter
    self._count = 0

    # Check diagonally LEFT TO RIGHT
    for r in range(self._rows):
      # diagonal column
      c = col - row + r

      if check(r, c):
        return True

    # reset counter
    self._count = 0

    # Check anti diagonally RIGHT TO LEFT
    for r in range(self._rows):
      # diagonal column
      c = row + col - r

      if check(r, c):
        return True

    return False


class Player:
  def __init__(self, name, color):
    self._name = name
    self._color = color

  def getName(self):
    return self._name
  
  def getColor(self):
    return self._color


class Game:
  def __init__(self, board, connectN):
    self._board = board
    self._connectN = connectN

    self._players = [
        Player("Player 1", GridPosition.RED), 
        Player("Player 2", GridPosition.YELLOW)
    ]

  def play(self):
    while True:
      for player in self._players:
        self._board.getBoard()

        print(f"{player.getName()}'s turn")
        color = player.getColor()

        colCnt = self._board.getColumnsCount()

        column = int(input(f"Enter Column between {0} and {colCnt - 1} to add piece: "))
        row = self._board.placeColor(column, color)

        if self._board.checkWin(self._connectN, row, column, color):
          return player


board = Board(4, 6)

board.getBoard()

game = Game(board, 4)

game.play()
