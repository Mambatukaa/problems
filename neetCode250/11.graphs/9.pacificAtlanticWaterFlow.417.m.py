""""
There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.



"""

# Time Complexity: O(N * M)
# Space Complexity: O(N * M)
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ROWS = len(heights)
        COLS = len(heights[0])

        pacific_reachable = set()
        atlantic_reachable = set()

        def dfs(row, col, reachable):
            reachable.add((row, col))

            for dr, dy in DIRECTIONS:
                new_row = row + dr
                new_col = col + dy

                if new_row < 0 or new_row >= ROWS or new_col < 0 or new_col >= COLS or (new_row, new_col) in reachable:
                    continue
                
                if heights[new_row][new_col] < heights[row][col]:
                    continue

                dfs(new_row, new_col, reachable)

            
        for r in range(ROWS):
            dfs(r, 0, pacific_reachable)
            dfs(r, COLS - 1, atlantic_reachable)
        
        for c in range(COLS):
            dfs(0, c, pacific_reachable)
            dfs(ROWS - 1, c, atlantic_reachable)
        

        return list(atlantic_reachable.intersection(pacific_reachable))




class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        DIRECTIONS = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ROWS = len(heights)
        COLS = len(heights[0])

        pacific_reachable = set()
        atlantic_reachable = set()

        def bfs(row, col, reachable):
            q = deque([[row, col]])

            while q:
                row, col = q.popleft()
                reachable.add((row, col))

                for dr, dy in DIRECTIONS:
                    new_row = row + dr
                    new_col = col + dy
    
                    if new_row < 0 or new_row >= ROWS or new_col < 0 or new_col >= COLS or (new_row, new_col) in reachable:
                        continue
                    
                    if heights[new_row][new_col] < heights[row][col]:
                        continue
    
                    reachable.add((new_row, new_col))
                    q.append([new_row, new_col])
            
        for r in range(ROWS):
            bfs(r, 0, pacific_reachable)
            bfs(r, COLS - 1, atlantic_reachable)
        
        for c in range(COLS):
            bfs(0, c, pacific_reachable)
            bfs(ROWS - 1, c, atlantic_reachable)
        

        return list(atlantic_reachable.intersection(pacific_reachable))



    
