

# Time Complexity: O(n^2)
# Space Complexity: O(1)
# NeetCode
def rotateImage(matrix):
  n = len(matrix)

  left = 0
  right = n - 1

  while left < right:
    # replace REVERSED ORDER TO USE ONLY ONE TEMP VARIABLE

    for i in range(right - left):
      top, bottom = left, right

      # save the top left
      topLeft = matrix[top][left + i]

      # move bottom left into top left
      matrix[top][left + i] = matrix[bottom - i][left]

      # move bottom right into bottom left
      matrix[bottom - i][left] = matrix[bottom][right - i]

      # move top right into bottom right
      matrix[bottom][right - i] = matrix[top + i][right]

      # move top left into top right
      matrix[top + i][right] = topLeft

    left += 1
    right -= 1

matrix = [[1,2,3],[4,5,6],[7,8,9]]

rotateImage(matrix)

print("res:", matrix)



"""

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix
and do the rotation.



Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]


1 2 3        7 4 1
4 5 6 ====>  8 5 2
7 8 9        9 6 3


*****************

Save the value using temp variable and replace the location by new value

1. Need to set boundaries using 4 pointers. Top, Bottom, Left, Right
2. Replace the value starts from the outer edge.


"""
