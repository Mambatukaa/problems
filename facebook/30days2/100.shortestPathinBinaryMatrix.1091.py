""""
0
grid[i][j] is 0 or 1Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

A clear path in a binary matrix is a path from the top-left cell (i.e., (0, 0)) to the bottom-right cell (i.e., (n - 1, n - 1)) such that:

All the visited cells of the path are 0.
All the adjacent cells of the path are 8-directionally connected (i.e., they are different and they share an edge or a corner).
The length of a clear path is the number of visited cells of this path.

 

Example 1:


Input: grid = [[0,1],[1,0]]
Output: 2
Example 2:


Input: grid = [[0,0,0],[1,1,0],[1,1,0]]
Output: 4
Example 3:

Input: grid = [[1,0,0],[1,1,0],[1,1,0]]
Output: -1
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 10



"""
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        # bfs with steps
        N = len(grid)


        DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1], [-1, -1], [-1, 1], [1, -1], [1, 1]]

        q = deque([[0, 0, 1]])

        visited = set()
        visited.add((0, 0))

        while q:
            row, col, step = q.popleft()

            if row == N - 1 and col == N - 1:
                return step

            for dr, dc in DIRECTIONS:
                newRow = row + dr
                newCol = col + dc

                if not (0 <= newRow < N and 0 <= newCol < N) or (newRow, newCol) in visited or grid[newRow][newCol] == 1:
                    continue
                
                visited.add((newRow, newCol))
                q.append([newRow, newCol, step + 1])

        return -1


        
