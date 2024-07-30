# Time Complexity: O(n)
# Space Complexity: O(n)
# DFS
def floodFill(image, sr, sc, color):
  m = len(image)
  n = len(image[0])

  mainColor = image[sr][sc]

  if mainColor == color:
    return image

  def dfs(row, col):
    # check row col is valid or not
    if row < 0 or col < 0 or row >= m or col >= n or image[row][col] != mainColor:
      return

    # replace the valid neighbor by color
    image[row][col] = color

    # check neighbors by 4 directionally

    # top
    dfs(row + 1, col)
    # bottom
    dfs(row - 1, col)

    # right
    dfs(row, col + 1)

    #left
    dfs(row, col - 1)

  dfs(sr, sc)

  return image


image = [
  [1, 1, 1],
  [1, 1, 0],
  [1, 0, 1]
]

print("Res:", floodFill(image, 1, 1, 3))


"""

image[sr][sc]
color


image = [
[1, 1, 1],
[1, 1, 0],
[1, 0, 1]
]

sr = 1
sc = 1
color = 2

Output:
  image = [
    [2, 2, 2],
    [2, 1, 0],
    [2, 0, 1]
  ]


Replace the neighbors who has same color as image[sr][sc] to color.

Starting point is image[sr][sc]. 4 - directionally neighbor

Return replaced grid




"""
