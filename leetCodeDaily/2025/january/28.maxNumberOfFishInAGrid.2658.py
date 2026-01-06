""""


You are given a 0-indexed 2D matrix grid of size m x n, where (r, c) represents:
• A land cell if (grid [r] [c] = 0, or
• A water cell containing (grid [r] [c] fish, if grid[r] [c] > 0.
A fisher can start at any water cell (r, c) and can do the following operations any number of times:
• Catch all the fish at cell (r, c) , or
• Move to any adjacent water cell.
Return the maximum number of fish the fisher can catch if he chooses his starting cell optimally, or 0 if no water cell exists.
An adjacent cell of the cell (r, c) , is one of the cells (r, c + 1), (г, c - 1), (r + 1, c) or (r - 1, c) if it exists.

Input: grid = [ [0,2,1,0], [4,0,0,3], [1,0,0,4], [0,3,2,0]]
Output: 7
Explanation: The fisher can start at cell (1,3) and collect 3 fish, then move to cell (2,3) and collect 4
fish.



Constraints:
• m = grid. length
n = grid [i]. length

• 1 < m, n <= 10

• 0 <= grid[i][j] <= 10

"""

# Time Complexity: O(n * m)
# Space Complexity: O(n * m)
# DFS
class Solution:
    def findMaxFish(self, grid) -> int:
        seen = set()

        ROWS = len(grid)
        COLS = len(grid[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or (r, c) in seen or grid[r][c] == 0:
                return 0

            seen.add((r, c))
            
            return grid[r][c] + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1)


        res = 0

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) not in seen and grid[r][c] != 0:
                    res = max(res, dfs(r, c))


        return res


grid = [[0,2,1,0], 
        [4,0,0,3], 
        [1,0,0,4], 
        [0,3,2,0]]


grid = [[1,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,1]]
solution = Solution()

print("res:", solution.findMaxFish(grid))
