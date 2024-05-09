# Time Complexity: O(n * m * l) l = land
# Space Complexity: O(l) l = land
# 20 minutes
# DFS
class Solution:
    def maxAreaOfIsland(self, grid):
      res = 0
      self.counter = 0

      m = len(grid)
      n = len(grid[0])

      def dfs(r, c):
        if r < 0 or c < 0 or r >= m or c >= n or grid[r][c] != 1:
          return
        
        self.counter += 1

        grid[r][c] = 0

        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)


      for r in range(m):
        for c in range(n):
          cur = 0

          if grid[r][c] == 1:
            self.counter = 0
            dfs(r, c)
            res = max(self.counter, res)
            
      return res

        
solution = Solution()

grid = [
        [0,0,1,0,0,0,0,1,0,0,0,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],
        [0,1,0,0,1,1,0,0,1,1,1,0,0],
        [0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],
        [0,0,0,0,0,0,0,1,1,0,0,0,0]
        ]
solution.maxAreaOfIsland(grid)
