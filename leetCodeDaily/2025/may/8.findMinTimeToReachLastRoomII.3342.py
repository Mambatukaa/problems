""""
There is a dungeon with n x m rooms arranged as a grid.

You are given a 2D array moveTime of size n x m, where moveTime[i][j] represents the minimum time in seconds when you can start moving to that room. You start from the room (0, 0) at time t = 0 and can move to an adjacent room. Moving between adjacent rooms takes exactly one second.

Return the minimum time to reach the room (n - 1, m - 1).

Two rooms are adjacent if they share a common wall, either horizontally or vertically.



Example 1:

Input: moveTime = [[0,4],[4,4]]

Output: 6

Explanation:

The minimum time required is 6 seconds.

At time t == 4, move from room (0, 0) to room (1, 0) in one second.
At time t == 5, move from room (1, 0) to room (1, 1) in one second.
Example 2:

Input: moveTime = [[0,0,0],[0,0,0]]

Output: 3

Explanation:

The minimum time required is 3 seconds.

At time t == 0, move from room (0, 0) to room (1, 0) in one second.
At time t == 1, move from room (1, 0) to room (1, 1) in one second.
At time t == 2, move from room (1, 1) to room (1, 2) in one second.
Example 3:

Input: moveTime = [[0,1],[1,2]]

Output: 3

 

Constraints:

2 <= n == moveTime.length <= 50
2 <= m == moveTime[i].length <= 50
0 <= moveTime[i][j] <= 109

"""

from collections import deque
from heapq import heapify, heappop, heappush


class Solution:
    # Time Complexity: O(mn * log(nm))
    # Space Complexity: O(mn)
    def minTimeToReach(self, moveTime) -> int:


        ROWS = len(moveTime)
        COLS = len(moveTime[0])


        q = [(0, 1, 0, 0)]

        heapify(q)

        visited = set()
        visited.add((0,0))


        while q:
            time, cost, row, col = heappop(q)

            if row == ROWS - 1 and col == COLS - 1:
                return time

            # collect neighbors

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                newRow = row + dx
                newCol = col + dy

                if newRow < 0 or newRow >= ROWS or newCol < 0 or newCol >= COLS or (newRow, newCol) in visited:
                    continue

                
                visited.add((newRow, newCol))
                new_time = max(time, moveTime[newRow][newCol]) + cost

                heappush(q, (new_time, 1 if cost == 2 else 2, newRow, newCol))


        

        
solution = Solution()        

moveTime = [[0,1],[1,2]]



moveTime =[[17,56], 
           [97,80]]

moveTime = [ [0,4]
            ,[4,4]]
moveTime = [[0,0,0, 0],[0,0,0,0]]
print("res:", solution.minTimeToReach(moveTime))
