from collections import deque

# Add solution using BFS
# Because we use BFS to find short path
# Time Complexity: O(n) n = v + e
# Space Complexity: O(n) n = v + e
# Got tips
class Solution:
    def islandsAndTreasure(self, grid):
      m = len(grid)
      n = len(grid[0])

      def isValid(r, c, seen):
          isInRange = r >= 0 and r < m and c >= 0 and c < n  

          return isInRange and grid[r][c] != -1 and (r,c) not in seen

      #              BOTTOM   TOP      RIGHT   LEFT
      DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]


      def bfs(r, c, dist, seen):
          queue = deque([[r, c, dist]])

          while len(queue):
              [row, col, currDis] = queue.popleft()
              print(row, col)

              if grid[row][col] == 0:
                  return currDis

              for [dx, dy] in DIRECTIONS:
                  newRow = row + dx
                  newCol = col + dy

                  print(newRow, newCol, isValid(newRow, newCol, seen))

                  if isValid(newRow, newCol, seen):
                      seen.add((newRow,newCol))
                      queue.append([newRow, newCol, currDis + 1])




      for r in range(m):
        for c in range(n):
          # found empty room
          if (grid[r][c] > 1):
            seen = set((r,c)) 
            print("row:", r, "col:", c)
            grid[r][c] = bfs(r, c, 0, seen)

      return grid


solution = Solution()


grid=[[2,0,2,2,2],
      [2,2,-1,2,2],
      [2,2,2,-1,2],
      [0,2,-1,2,2],
      [2,2,2,0,2]]




print(solution.islandsAndTreasure(grid))
        




# Fill empty room with the distance to its nearest gate


"""

  4 directional dfs find nearest gate which is 0


""" 
