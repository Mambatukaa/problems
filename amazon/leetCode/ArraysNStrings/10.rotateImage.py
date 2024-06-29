# naive approach
# Time Complexity: (n^2)
# Space Complexity: (n^2)
def rotateImage(matrix):
  dic = {}
  n = len(matrix)

  # build dic
  for r in range(n):
    dic[r] = matrix[r].copy()

  for row in dic:
    currentRow = dic[row]
    col = n - 1 - row

    for r in range(n):
      matrix[r][col] = currentRow[r]


matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
rotateImage(matrix)
print(matrix)

"""

Input: matrix = [[1, 2, 3], 
                 [4, 5, 6], 
                 [7, 8, 9]]

        Output: [[7, 4, 1], 
                 [8, 5, 2], 
                 [9, 6, 3]]


            0 1 2

         0: 1 2 3
         1: 4 5 6
         2: 7 8 9


row: 0, col: 2
row: 1, col: 1
row: 2, col: 0


row: 0, col: n - 1
row: 1, col: n - 2
row: 2, col: n - 3



map = {
  0: [1, 2, 3]
  1: [4, 5, 6]
  2: [7, 8, 9]
}

for key in keys:
  curr = map[key]

  row = key
  col = n - key - 1

  for i in range(row):
    matrix[i][col] = curr[i]


"""
