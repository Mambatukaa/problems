"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.



""""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])


        def dfs(row, col):
            # check map out of bounds or water
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or grid[row][col] == "0":
                return

            # mark visited land
            grid[row][col] = "0"

            # TOP
            dfs(row - 1, col)
            # BOTTOM
            dfs(row + 1, col)
            # RIGHT
            dfs(row, col + 1)
            # LEFT
            dfs(row, col - 1)

        res = 0

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    # land is found
                    res += 1

                    # visit connected lands

                    dfs(row, col)

        return res


       
        