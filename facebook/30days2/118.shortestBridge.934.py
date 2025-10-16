# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        N = len(grid)

        #              right    left    bottom  top
        DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(row, col):
            bfs_queue.append([(row, col), 0])
            grid[row][col] = 2

            for dr, dc in DIRECTIONS:
                newRow = row + dr
                newCol = col + dc

                if 0 <= newRow < N and 0 <= newCol < N and grid[newRow][newCol] == 1:
                    dfs(newRow, newCol)

        first_row = -1
        first_col = -1
        # mark first island's neighbors
        for row in range(N):
            for col in range(N):
                if grid[row][col] == 1:
                    first_row = row
                    first_col = col
                    break

        # mark first_island and add neighbors to the queue
        bfs_queue = deque([])
        dfs(first_row, first_col)

        while bfs_queue:
            size = len(bfs_queue)

            for _ in range(size):
                (row, col), distance = bfs_queue.popleft()

                for dr, dc in DIRECTIONS:
                    newRow = row + dr
                    newCol = col + dc

                    if 0 <= newRow < N and 0 <= newCol < N:
                        if grid[newRow][newCol] == 1:
                            return distance
                        elif grid[newRow][newCol] == 0:
                            bfs_queue.append([(newRow, newCol), distance + 1])
                            grid[newRow][newCol] -= 1

        return -1










"""




[0,1,0],
[0,0,0],
[0,0,1]



[1,1,1,1,1],
[1,0,0,0,1],
[1,0,2,0,1],
[1,0,0,0,1],
[1,1,1,1,1]

[
    
[2, 2, 2, 2, 2], 
[2, 0, 0, 0, 2], 
[2, 0, 1, 0, 2], 
[2, 0, 0, 0, 2], 
[2, 2, 2, 2, 2]]



1. Find the first island and mark the part of the islands

2. Find the second island and reach the part of the first island using the bfs or dfs

3. If the neighbor is zero increase the current_flip by one and add to the queue
""" 
