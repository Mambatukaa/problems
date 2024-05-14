from collections import deque

# Naive Brute force
# Time Complexity: O(n * m)^2
# Space Complexity: O(n * m)^2
# 1 hour
class Solution:
    def pacificAtlantic(self, heights):
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







# Time Complexity: O(n * m)
# Space Complexity: O(n * m)
# Neet code algorithm
class Solution:
    def pacificAtlantic(self, heights):
      ROWS = len(heights)
      COLS = len(heights[0])


      def dfs(r, c, seen, prev): 
        if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r,c) in seen or heights[r][c] < prev:
          return
        
        seen.add((r,c))

        curr = heights[r][c]
        
        dfs(r + 1, c, seen, curr)
        dfs(r - 1, c, seen, curr)
        dfs(r, c + 1, seen, curr)
        dfs(r, c - 1, seen, curr)
      
      pacific = set()
      atlantic = set()

      for c in range(COLS):
      # Pacific ocean TOP
        dfs(0, c, pacific, heights[0][c])
      # Atlantic ocean RIGHT
        dfs(ROWS - 1, c, atlantic, heights[ROWS-1][c])
      
      for r in range(ROWS):
      # Pacific ocean LEFT
        dfs(r, 0, pacific, heights[r][0])

      # Atlantic ocean Bottom
        dfs(r, COLS - 1, atlantic, heights[r][COLS-1])

      res = []

      for r in range(ROWS):
          for c in range(COLS):
              if (r,c) in pacific and (r,c) in atlantic:
                  res.append([r,c])
     
      return res


solution = Solution1()

heights = [

        [1,2,2,3,5],
        [3,2,3,4,4],
        [2,4,5,3,1],
        [6,7,1,4,5],
        [5,1,1,2,4]

        ]

print(solution.pacificAtlantic(heights))


"""

STARTED FROM OCEAN SITE AND ADD POSSIBLE VALUES TO THE EACH OCEAN
    COMPARE OCEANS THE DUPLICATED VALUES WILL BE ANSWER..



"""

