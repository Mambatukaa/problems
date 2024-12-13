# Graph initial 



class Solution:
    # Iterative
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def numIslands(self, grid):
        self.res = 0
        ROWS = len(grid)
        COLS = len(grid[0])

        DIRECTIONS = [[1, 0],[-1, 0],[0, 1],[0, -1]]

        def dfs(row, col):
            stack = [[row, col]]

            while stack:
                currRow, currCol = stack.pop()
                grid[currRow][currCol] = "0"

                for dx, dy in DIRECTIONS:
                    newRow, newCol = currRow + dx, currCol + dy

                    if newRow < 0 or newRow >= ROWS or newCol < 0 or newCol >= COLS or grid[newRow][newCol] == "0":
                        continue

                    stack.append([newRow, newCol])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    self.res += 1
                    
                    dfs(r, c)
        
        return self.res

    # Recursive
    # Time Complexity: O(n)
    # Space Complexity: O(n)
    def numIslandsII(self, grid):
        self. res = 0
        ROWS = len(grid)
        COLS = len(grid[0])
        

        def dfs(row, col):
            if row < 0 or col < 0 or row >= ROWS or col >= COLS or grid[row][col] == "0":
                return

            grid[row][col] = "0"

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)


        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    self.res += 1
                    
                    dfs(r, c)
        
        return self.res


grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","1"]
]

solution = Solution()
#print("Res:", solution.numIslands(grid))
print("Res:", solution.numIslandsII(grid))
        
