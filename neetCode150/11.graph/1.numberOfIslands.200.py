from collections import deque

# Time Complexity: O(n * m * l) l = land
# Space Complexity: O(n * m)
# 30 minutes
class Solution:
    def numIslands(self, grid):

        m = len(grid) # row length
        n = len(grid[0]) # col length

        #               TOP     BOTTOM   LEFT    RIGHT
        DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def isValid(r, c):
            return r >= 0 and r < m and c >= 0 and c < n and grid[r][c] == "1"

        def bfs(r, c, seen):
            queue = deque([[r, c]])

            while len(queue):
                [row, col] = queue.popleft()

                for [dx, dy] in DIRECTIONS:
                    newRow = row + dx
                    newCol = col + dy

                    if isValid(newRow, newCol) and seen[newRow][newCol] == False:
                        seen[newRow][newCol] = True
                        queue.append([newRow, newCol])

        # island counter
        counter = 0

        # seen to track already visited elements
        seen = [[False for c in range(n)] for r in range(m)]

        # iterate through grid
        for row in range(m):
            for col in range(n):
                # if element is land and not visited call bfs
                if grid[row][col] == "1" and not seen[row][col]:
                    seen[row][col] = True
                    # found new island
                    counter += 1
                    bfs(row, col, seen)

        return counter

solution = Solution()

grid = [["1","0","1","1","0","1","1"]]



# Easy dfs

def numIslands(grid):
    m = len(grid)
    n = len(grid[0])


    def dfs(r, c):
        if r < 0 or c < 0 or r >= m or c >= n or grid[r][c] != "1":
            return

        grid[r][c] = "$"

        dfs(r + 1, c)
        dfs(r - 1, c)
        dfs(r, c + 1)
        dfs(r, c - 1)

    counter = 0

    for r in range(m):
        for c in range(n):

            if grid[r][c] == "1":
                counter += 1

                dfs(r, c)
    
    return counter

print(numIslands(grid))

"""
 
 Adjacency Matrix 

 Example 1:

 [1, 1, 1, 1, 0],
 [1, 1, 0, 1, 0],
 [1, 1, 0, 0, 0],
 [0, 0, 0, 0, 0],

 Output: 1


 Example 2:

 [1, 1, 0, 0, 0],
 [1, 1, 0, 0, 0],
 [0, 0, 1, 0, 0],
 [0, 0, 0, 1, 1],

 Output: 3


 1. Iterate through matrix.
  
    Check is land found.
      If land found 
        check is there any surrounded land. Search 4 directions
          if surrounded land found mark the land by seen
      
    Do the above steps until the iteration finishes

    1. Use set or array to check the element visited or not
    2. Do BFS search or DFS search
    3. Use counter to count total islands



"""
