from collections import deque

# Naive
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
      ROWS = len(heights)
      COLS = len(heights[0])

      #              TOP     BOTTOM   RIGHT   LEFT
      DIRECTIONS = [ [1, 0], [-1, 0], [0, 1], [0, -1] ]

      def bfs(r, c, seen):
        queue = deque([[r, c]])

        pacific = False
        atlantic = False

        while queue:
          [row, col] = queue.popleft()
          curr = heights[row][col]

          for [dx, dy] in DIRECTIONS:
            newRow = row + dx
            newCol = col + dy

            if pacific and atlantic:
              return True

            # pacific ocean
            if newRow < 0 or newCol < 0:
              pacific = True
              continue

            if newRow >= ROWS or newCol >= COLS:
              atlantic = True
              continue
            
            if (newRow,newCol) not in seen and heights[newRow][newCol] <= curr:
              queue.append([newRow, newCol])
              seen.add((newRow,newCol))
        
        return pacific and atlantic

      res = []

      for r in range(ROWS):
        for c in range(COLS):
          seen = set()
          
          if bfs(r, c, seen):
            res.append([r,c])

      return res       

"""

neighboring celss directly north, south, east, and west 
  if the neighboring cell's height is less than or equal to the current cell's height. 
    Water can flow from any cell adjacent to an ocean into the ocean.


Input: heights = [ 
 [ 1, 2, 2, 3, 5 ],
 [ 3, 2, 3, 4, 4 ], 
 [ 2, 4, 5, 3, 1 ], 
 [ 6, 7, 1, 4, 5 ], 
 [ 5, 1, 1, 2, 4 ] 
 ] 


 1. Started from Pacific ocean.
      The current cell can reach the PACIFIC OCEAN (-1, y) or (x, -1) AND ATLANTIC OCEAN (ROWS, y), (x, COLS) to 
        adding the valid neighbors which is equal or less than current cell


"""
