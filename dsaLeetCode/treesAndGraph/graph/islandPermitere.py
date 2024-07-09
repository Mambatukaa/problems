# Time Complexity: O(n * m)
# Space Complexity: O(1)
def islandPerimeter(grid):
  perimeter = 0
  m = len(grid)
  n = len(grid[0])

  for row in range(m):
    for col in range(n):

      if grid[row][col] == 1:

        perimeter += 4 * grid[row][col]

        # top
        if row > 0: perimeter -= 1 if grid[row - 1][col] == 1 else 0

        # bottom
        if row < m - 1: perimeter -= 1 if grid[row + 1][col] else 0

        # left
        if col > 0: perimeter -= 1 if grid[row][col - 1] else 0

        # right
        if col < n - 1 : perimeter -= 1 if grid[row][col + 1] else 0


  return perimeter



grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]

print("res:", islandPerimeter(grid))

"""

There is exactly one island. Find the Perimeter of an ISLAND.

Perimeter = (total windows + 1) * 2


find total windows * 2



1. Find total possible perimeter
2. Check the 4 directions and decrease by 1 or 0


"""
