# Time Complexity: O(n + m)
# Space Complexity: O(n + m)
# DFS
class Solution:
  def numberOfEnclaves(self, grid):
    self.totalWalkedLands = 0
    totalLands = 0

    m = len(grid)
    n = len(grid[0])

    seen = [[False for i in range(n)] for _ in range(m)]

    def dfs(row, col, seen):
      if row < 0 or col < 0 or row > m - 1 or col > n - 1 or grid[row][col] == 0 or seen[row][col]:
        return

      self.totalWalkedLands += 1
      seen[row][col] = True

      # top
      dfs(row - 1, col, seen)

      # bottom
      dfs(row + 1, col, seen)

      # left
      dfs(row, col - 1, seen)

      # right
      dfs(row, col + 1, seen)

    # iterate through bounderies
    for row in range(m):
      for col in range(n):

        if grid[row][col] == 1:
          totalLands += 1

          # starting from bounderies
          if row == 0 or row == m - 1 or col == 0 or col == n - 1 and not seen[row][col]:
            dfs(row, col, seen)

    return totalLands - self.totalWalkedLands 

  # Time Complexity: O(n + m)
  # Space Complexity: O(n + m)
  # NO additional variables needed
  def numberOfEnclavesII(self, grid):
    m = len(grid)
    n = len(grid[0])

    def dfs(row, col):
      if row < 0 or col < 0 or row > m - 1 or col > n - 1 or grid[row][col] == 0:
        return

      grid[row][col] = 0

      # top
      dfs(row - 1, col)
      # bottom
      dfs(row + 1, col)
      # left
      dfs(row, col - 1)
      # right
      dfs(row, col + 1)

    # iterate through bounderies
    for row in range(m):
      for col in range(n):
        if grid[row][col] == 1:
          # starting from bounderies
          if row == 0 or row == m - 1 or col == 0 or col == n - 1:
            dfs(row, col)

    return sum((sum(row) for row in grid))

grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0], [0,0,0,0]]
solution = Solution()
print("res:", solution.numberOfEnclavesII(grid))


"""

1. Find the total number of cells we cannot walk starts walk from boundary.


  m = len(row), n = len(col)

2. row = 0, col = 0, row = m - 1, col = n - 1 BOUNDARIES

3. Start to walk from every boundaries and try to walk on neighbors of 4 directions. DFS OR BFS
4. Track total numbers of walked lands
5. Return total num of lands - totalWalkedLands



"""
