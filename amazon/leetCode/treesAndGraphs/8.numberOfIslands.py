# Time Complexity: O(m * n)
# Space Complexity: O(m * n)
# Space complexity : worst case O(M×N) in case that the grid map
# is filled with lands where DFS goes by M×N deep.



def numberOfIslands(grid):
  # row length
  m = len(grid)
  # col length
  n = len(grid[0])


  def dfs(row, col):
    # check the ceil is valid or not
    if row < 0 or col < 0 or row >= m or col >= n or grid[row][col] == "0":
      return

    grid[row][col] = '0'

    # call neighbors

    # TOP
    dfs(row + 1, col)
    # Bottom
    dfs(row - 1, col)
    # Right
    dfs(row, col + 1)
    # Left
    dfs(row, col - 1)

  res = 0

  for row in range(m):
    for col in range(n):
      if grid[row][col] == "1":
        res += 1
        dfs(row, col)


  return res


grid = [
  ["1","1","1","0","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]

print("Res:", numberOfIslands(grid))


"""
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1




Return the total number of ISLANDS. 1 is land 0 is water.




1. DO DFS or BFS
"""
