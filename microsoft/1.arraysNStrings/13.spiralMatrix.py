# Time Complexity: O(n * m)
# Space Complexity: O(n * m)
def spiralMatrix(matrix):
  ROWS = len(matrix)
  COLS = len(matrix[0])

  res = []

  l = 0
  r = COLS - 1

  top = 0
  bottom = ROWS - 1


  while top <= bottom and l <= r:
    # left to right
    # TL to TR
    for i in range(l, r + 1):
      res.append(matrix[top][i])

    # top to bottom
    # TR to BR
    for i in range(top + 1, bottom + 1):
      res.append(matrix[i][r])

    # right to left
    # BR to BL
    if top != bottom:
      for i in range(r - 1, l - 1, -1):
        res.append(matrix[bottom][i])

    # bottom to top
    # BL to Top L
    if l != r:
      for i in range(bottom - 1, top, -1):
        res.append(matrix[i][l])

    l += 1
    r -= 1
    top += 1
    bottom -= 1

  return res


matrix = [
    [1, 2],
    [3, 4],
    [5, 6],
    [7, 8]
    ]

print("Res:", spiralMatrix(matrix))

"""

Given an m x n matrix, return all elements of the matrix in spiral order.

"""
