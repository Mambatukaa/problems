""""
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

 

Example 1:


Input: grid = [[1,3,1],[1,5,1],[4,2,1]]
Output: 7
Explanation: Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
Example 2:

Input: grid = [[1,2,3],[4,5,6]]
Output: 12
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 200
0 <= grid[i][j] <= 200
 








"""
# Dijakstra
# Time Complexity: O(N * M)
# SPACE Complexity: O(N * M)
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        # bfs with queue
        # curr_sum, curr_row, curr_col
        # until reach the lastRow and lastCol

        heap = []
        heappush(heap, (grid[0][0], 0, 0))

        #              right   down
        DIRECTIONS = [(0, 1), (1, 0)]

        seen = set()

        while heap:
            S, c_row, c_col = heappop(heap)

            if c_row == ROWS - 1 and c_col == COLS - 1:
                return S

            for dr, dc in DIRECTIONS:
                n_row = c_row + dr
                n_col = c_col + dc

                if not (n_row < ROWS and n_col < COLS) or (n_row, n_col) in seen:
                    continue
                
                seen.add((n_row, n_col))
                heappush(heap, (S + grid[n_row][n_col], n_row, n_col))

        
