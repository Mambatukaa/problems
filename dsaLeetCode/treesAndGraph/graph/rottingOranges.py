from collections import deque

# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
# BFS
class Solution:
  def orangesRotting(self, grid):
    # rows
    m = len(grid)

    # columns
    n = len(grid[0])
    q = deque([])

    freshOranges = 0
    minutes = 0

    seen = set()

    for row in range(m):
      for col in range(n):
        if grid[row][col] == 1:
          # count fresh oranges
          freshOranges += 1

        if grid[row][col] == 2:
          # count rotten oranges
          q.append([row,col])
          seen.add((row,col))

    # base case
    if not freshOranges:
      return 0


    #               TOP   BOTTOM     RIGHT   LEFT
    DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    # start to rote oranges

    while q:
      if not freshOranges:
        return minutes 

      size = len(q)

      for _ in range(size):
        # start to rote neighbors
        row, col = q.popleft()

        for dy, dx in DIRECTIONS:
          newRow = row + dy
          newCol = col + dx

          # check new cell is valid or not
          if newRow < 0 or newCol < 0 or newRow > m - 1 or newCol > n - 1 or grid[newRow][newCol] == 0 or (newRow, newCol) in seen:
            continue

          seen.add((newRow, newCol))
          q.append([newRow, newCol])
          freshOranges -= 1

      minutes += 1

    return -1

solution = Solution()

#grid = [[2,1,1],[1,1,0],[0,1,1]]
grid = [[2,1,1],[0,1,1],[1,0,1]]
#grid = [[0,2]]

print(solution.orangesRotting(grid))



"""

0: representing an empty cell.
1: representing a fresh orange.
2: representing a rotten orange.



Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. 
  If this is impossible, return -1.


[2,1,1]
[1,1,0]
[0,1,1]


Rotten orange can rote fresh orange 4-directionally

1. Since rotten orange can rote neighbors BFS or DFS search.
2. Need to cound fresh oranges.
    If freshOranges == 0:
      return 0

3. There can be rotten orange 0 to n

4. Count fresh oranges and rotten oranges





Constraints:
  m == grid.length
  n == grid[i].length
  1 <= m, n <= 10
  grid[i][j] is 0, 1, or 2.

"""

        

