# Naive approach
# Time Complexity: O(n * m)
# Space Complexity: O(n + m)
def setMatrixZeroes(matrix):
  rowsToReplace = set()
  colsToReplace = set()

  ROWS = len(matrix)
  COLS = len(matrix[0])

  for row in range(ROWS):
    for col in range(COLS):
      if matrix[row][col] == 0:
        rowsToReplace.add(row)
        colsToReplace.add(col)


  # iterate through rowsToReplace and colsToReplace and replace by 0

  for row in rowsToReplace:
    for col in range(COLS):
      matrix[row][col] = 0

  for col in colsToReplace:
    for row in range(ROWS):
      matrix[row][col] = 0


  
matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]


setMatrixZeroes(matrix)

print(matrix)


"""


Given an m x n integer matrix matrix, if an element is 0 1, set its entire row and column to 0 's.

  You must do it in place.



Iterate through matrix and collect zeroes positions. 
  Then iterate through zeroes positions and replace the row and col by 0;

"""
