from collections import deque

# Bfs
# Time Complexity: O(n * m)
# Space Complexity: O(n * m)

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
      m = len(grid)
      n = len(grid[0])

      fresh, time = 0, 0
      queue = deque([])

      for r in range(m):
        for c in range(n):
          # found fresh orange
          if grid[r][c] == 1:
            fresh += 1
          if grid[r][c] == 2:
            queue.append([r,c])

      #             BOTTOM    TOP     RIGHT   LEFT
      DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]

      def isValid(r, c):
        return r >= 0 and r < m and c >= 0 and c < n and grid[r][c] == 1

      while queue and fresh > 0:
        size = len(queue)

        for i in range(size):
          [row, col] = queue.popleft()

          for [dx, dy] in DIRECTIONS:
            newRow = row + dx
            newCol = col + dy

            if isValid(newRow, newCol):
              grid[newRow][newCol] = 2
              fresh -= 1
              queue.append([newRow, newCol])

        time += 1

      return time if not fresh else -1

"""

0 - empty cell
1 - fresh orange
2 - a rotten orange


Every minute 4-directionally adjacent to a rotten orange becomes rotten.


EXAMPLE 1:

grid = [
  [2, 1, 1],
  [1, 1, 0],
  [0, 1, 1]
]

output: 4


EXAMPLE 2:

grid = [
  [2, 1, 1],
  [0, 1, 1],
  [1, 0, 1]
]

output: -1
Explanation: The orange in the bottom left corner is never rotten because rotting only happens 4-directionally


"""
