"""

You are given a 0-indexed 2D array grid of size 2 x n, where grid [r] [c] represents the number of points at
position (r, c) on the matrix. Two robots are playing a game on this matrix.

Both robots initially start at (0, 0) and want to reach (1, n-1) . Each robot may only move to the right ( (r, c)
to (r, c + 1) ) or down ((r, c) to (r + 1, c)).

At the start of the game, the first robot moves from (0, 0) to (1, n-1), collecting all the points from the cells
on its path. For all cells (r, c) traversed on the path, grid[r] [c] is set to 0. Then, the second robot moves
from (0, 0) to (1, n-1), collecting the points on its path. Note that their paths may intersect with one another.

The first robot wants to minimize the number of points collected by the second robot. In contrast, the second
robot wants to maximize the number of points it collects. If both robots play optimally, return the number of
points collected by the second robot.




Constraints:
• grid.length == 2
• n == grid[r].length
• 1 < n <= 5 * 10^4
• 1 < grid[r][c] <= 10^5

"""


# Prefix sum
# Time Complexity: O(n)
# Space Complexity: O(n)
class Solution:
    def gridGame(self, grid):
        n = len(grid[0])
        prefixRow1 = grid[0].copy()
        prefixRow2 = grid[1].copy()

        # convert grid to prefix
        for i in range(1, n):
            prefixRow1[i] += prefixRow1[i - 1]
            prefixRow2[i] += prefixRow2[i - 1]

        res = float('inf')

        for i in range(n):
            top = prefixRow1[-1] - prefixRow1[i]
            bottom = prefixRow2[i - 1] if i > 0 else 0
            secondRobot = max(top, bottom)

            res = min(res, secondRobot)

        return res


solution = Solution()

grid = [[1, 1, 1, 15],
        [2, 3, 3, 1]
        ]

print("res:", solution.gridGame(grid))







