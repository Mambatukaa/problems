""""
You are given an m x n grid rooms initialized with these three possible values.

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

 

Example 1:


Input: rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
Output: [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
Example 2:

Input: rooms = [[-1]]
Output: [[-1]]
 

Constraints:

m == rooms.length
n == rooms[i].length
1 <= m, n <= 250
rooms[i][j] is -1, 0, or 231 - 1.

"""

from collections import deque

class Solution:
    def islandsAndTreasure(self, grid) -> None:
        ROWS = len(grid)
        COLS = len(grid[0])


        # start from the gates

        q = deque([])
        visited = set()

        for r in range(len(grid)):
            for c in range(len(grid[0])):

                if grid[r][c] == 0:
                    q.append([r, c])
                    visited.add((r,c))


        def addRooms(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == -1 or (r, c) in visited:
                return

            visited.add((r, c))
            q.append([r, c])

        dist = 0

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist

                addRooms(r + 1, c)
                addRooms(r - 1, c)
                addRooms(r, c + 1)
                addRooms(r, c - 1)
            dist += 1

rooms = [[2147483647,-1,0,2147483647],
         [2147483647,2147483647,2147483647,-1],
         [2147483647,-1,2147483647,-1],
         [0,-1,2147483647,2147483647]]


solution = Solution()
print("res:", solution.islandsAndTreasure(rooms))

print(rooms)
