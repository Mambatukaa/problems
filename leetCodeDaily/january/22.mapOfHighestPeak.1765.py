
from collections import deque


# BFS solution
# Time Complexity: O(n * m)
# Space Complexity: O(n * m)
# 45 minutes
class Solution:
    def highestPeak(self, isWater):
        # find water and update the land neighbors
        queue = deque()
        visited = set()

        ROWS = len(isWater)
        COLS = len(isWater[0])

        #             DOWN     UP       RIGHT   LEFT
        DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for r in range(ROWS):
            for c in range(COLS):

                # water cell
                if isWater[r][c] == 1:
                    isWater[r][c] = 0
                    visited.add((r, c))
                    queue.append([r, c])

        # add neighbor to the visited and queue
        # Do BFS through queue and update the unvisited nodes and add to the visited and also add to the queue
        while queue:
            currRow, currCol = queue.popleft()
            value = isWater[currRow][currCol]

            for dy, dx in DIRECTIONS:
                newRow = currRow + dy
                newCol = currCol + dx

                if newRow < 0 or newCol < 0 or newCol >= COLS or newRow >= ROWS or (newRow, newCol) in visited:
                    continue

                isWater[newRow][newCol] = value + 1
                visited.add((newRow, newCol))
                queue.append([newRow, newCol])

        return isWater

solution = Solution()

isWater = [[0,1],
           [0,0]]

isWater = [[1,1],
           [0,0]]
isWater =[[0, 1, 0, 0], [1, 0, 1, 0], [0, 0, 0, 0], [0, 0, 0, 0]]


print("res:", solution.highestPeak(isWater))

