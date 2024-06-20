from collections import deque

# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
def snakesToLadders(board):
  length = len(board)

  # reverse the board to make calculation more easier
  board.reverse()

  def intToPos(square):
    row = (square - 1) // length
    col = (square - 1) % length

    # row is odd
    if row % 2:
      col = length - 1 - c
      
    return [row, col]

  q = deque() # [square, moves]

  q.append([1, 0])
  visit = set()

  while q:
    square, moves = q.popleft()

    # role the dice and add neighbors

    for i in range(1, 7):
      nextSquare = square + i

      # get coordinate
      r, c = intToPos(nextSquare)

      if board[r][c] != -1:
        # this value will be our shortcut
        nextSquare = board[r][c]

      # found solution
      if nextSquare == length * length:
        return moves + 1

      if nextSquare not in visit:
        visit.add(nextSquare)
        q.append([nextSquare, moves + 1])


  return -1

board = [
    [-1,-1,-1,-1,-1,-1], # 6 <-
    [-1,-1,-1,-1,-1,-1], # 5 ->
    [-1,-1,-1,-1,-1,-1], # 4 <-
    [-1,35,-1,-1,13,-1], # 3 -> 
    [-1,-1,-1,-1,-1,-1], # 2 <-
    [-1,15,-1,-1,-1,-1]  # 1 ->
] 

b = [

    [15, 26, 27, 28, 29, 30], 
    [24, 23, 22, 21, 20, 19],
    [13, 14, 15, 16, 17, 18],
    [12, 11, 10,  9,  8,  7],
    [ 1,  2,  3,  4,  5,  6]

    ]

print(b)

b.reverse()
print(b)


"""

n = 6
      0  1  2  3  4  5

0:   36 35 34 33 32 31
1:   25 26 27 28 29 30
2:   24 23 22 21 20 19
3:   13 14 15 16 17 18
4:   12 11 10  9  8  7
5:   1   2  3  4  5  6


starting point = [5][0]


starting point = last row first column



1. Start from 1 and add 1 neighbors to the queue

2. if neighbor is going to jump add the jump number to the queue

3. Add neighbors and add neighbors neighbors until reach the last element.

4. The first 


Save the nodes that we can reach each steps height is our response

if there is no answer return -1

"""
