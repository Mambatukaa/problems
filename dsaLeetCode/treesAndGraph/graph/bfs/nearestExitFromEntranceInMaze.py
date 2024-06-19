from collections import deque

class Solution:
    def nearestExit(self, maze, entrance) -> int:
      # row length
      m = len(maze)
      # col length
      n = len(maze[0])


      #              BOTTOM   UP      LEFT      RIGHT
      DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]]
      

      # to find shortest path BFS will be used

      def bfs(row, col, visited):
        queue = deque([[row, col, 0]])

        while len(queue):
          [currRow, currCol, currSteps] = queue.popleft()

          for [dy, dx] in DIRECTIONS:
            newRow = currRow + dy
            newCol = currCol + dx

            # check new row and column in range
            if newRow >= 0 and newCol >= 0 and newRow < m and newCol < n and maze[newRow][newCol] == "." and visited[newRow][newCol] == 0:
              if newRow == 0 or newCol == 0 or newRow == m - 1 or newCol == n - 1:
                return currSteps + 1

              visited[newRow][newCol] = 1
              queue.append([newRow, newCol, currSteps + 1])

        return -1


      visited = [[0 for i in range(n)] for j in range(m) ]
      visited[entrance[0]][entrance[1]] = 1


      return bfs(entrance[0], entrance[1], visited)




solution = Solution()

maze = [
        ["+",".","+","+","+","+","+"],
        ["+",".","+",".",".",".","+"],
        ["+",".","+",".","+",".","+"],
        ["+",".","X",".","+",".","+"],
        ["+","+","+","+","+",".","+"]]

entrance = [3,2]


"""
+ = walls
. = empty cells



find the NUMBER OF STEPS to the NEAREST EXIT.

if no such path exists return -1

"""



print('res:', solution.nearestExit(maze, entrance))
        
