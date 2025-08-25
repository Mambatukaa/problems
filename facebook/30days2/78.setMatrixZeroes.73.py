"""
73. Set Matrix Zeroes
Solved
Medium
Topics
premium lock icon
Companies
Hint
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

 

Example 1:


Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]
Example 2:


Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

Constraints:

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
 

Follow up:

A straightforward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?


"""


"""

use first cell of every column and row as a flag. This flag would determine whether a row or column has been set to zero. This means for every cell instead of going to M+N cells and setting it to zero we just set the flag in two cells.








"""

class Solution:
def setZeroes(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """

    R = len(matrix)
    C = len(matrix[0])

    is_col = False

    for r in range(R):
        if matrix[r][0] == 0:
            is_col = True

        for c in range(1, C):
            if matrix[r][c] == 0:
                matrix[r][0] = 0
                matrix[0][c] = 0


    for r in range(1, R):
        for c in range(1, C):
            if not matrix[r][0] or not matrix[0][c]:
                matrix[r][c] = 0

    if matrix[0][0] == 0:
        for c in range(C):
            matrix[0][c] = 0

    if is_col:
        for r in range(R):
            matrix[r][0] = 0
