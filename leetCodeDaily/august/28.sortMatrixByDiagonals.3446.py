"""
he diagonals with a black arrow must be non-increasing, so [0, 2] is changed to [2, 0]. The other diagonals are already in the correct order.

Example 3:

Input: grid = [[1]]

Output: [[1]]

Explanation:

Diagonals with exactly one element are already in order, so no changes are needed.

 

Constraints:

grid.length == grid[i].length == n
1 <= n <= 10
-105 <= grid[i][j] <= 105You are given an n x n square matrix of integers grid. Return the matrix such that:

The diagonals in the bottom-left triangle (including the middle diagonal) are sorted in non-increasing order.
The diagonals in the top-right triangle are sorted in non-decreasing order.
 

Example 1:

Input: grid = [[1,7,3],[9,8,2],[4,5,6]]

Output: [[8,2,3],[9,6,7],[4,5,1]]

Explanation:



The diagonals with a black arrow (bottom-left triangle) should be sorted in non-increasing order:

[1, 8, 6] becomes [8, 6, 1].
[9, 5] and [4] remain unchanged.
The diagonals with a blue arrow (top-right triangle) should be sorted in non-decreasing order:

[7, 2] becomes [2, 7].
[3] remains unchanged.
Example 2:

Input: grid = [[0,1],[1,2]]

Output: [[2,1],[1,0]]

Explanation:



T

"""

# Time Complexity: O(n^2 log n)
# Space Complexity: O(n)
class Solution:
    def sortMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)

        for r in range(n):
            tmp = []

            for c in range(n - r):
                tmp.append(grid[r + c][c])

            tmp.sort(reverse=True)

            for c in range(n - r):
                grid[r + c][c] = tmp[c]
        
        for c in range(1, n):
            tmp = []

            for r in range(n - c):
                tmp.append(grid[r][c + r])
            tmp.sort()

            for r in range(n - c):
                grid[r][c + r] = tmp[r]
                
        return grid


        


""""
    0 1 2

 0: 1 7 3
 1: 9 8 2
 2: 4 5 6

 0,0 -> 1, 1 -> 2, 2
 1,0 -> 2, 1
 2:0 

 ------------------------------------

 0,1 -> 1, 2
 0,2









"""
