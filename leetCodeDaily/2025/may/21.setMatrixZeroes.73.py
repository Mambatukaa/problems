""""
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

# Time Complexity: O(n * m)
# Space Complexity: O(1)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """


        zeroInFirstCol = False

        ROWS = len(matrix)
        COLS = len(matrix[0])

        for row in range(ROWS):
            if matrix[row][0] == 0 and not zeroInFirstCol:
                zeroInFirstCol = True

            for col in range(1, COLS):
                if matrix[row][col] == 0:
                    # flag
                    matrix[0][col] = 0
                    matrix[row][0] = 0

        
        for row in range(1, ROWS):
            for col in range(1, COLS):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        if matrix[0][0] == 0:
            for col in range(1, COLS):
                matrix[0][col] = 0

        if zeroInFirstCol:
            for row in range(ROWS):
                matrix[row][0] = 0
            

                



        
# Less iteration
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """


        zeroInFirstCol = False

        ROWS = len(matrix)
        COLS = len(matrix[0])

        for row in range(ROWS):
            if matrix[row][0] == 0 and not zeroInFirstCol:
                zeroInFirstCol = True

            for col in range(1, COLS):
                if matrix[row][col] == 0:
                    # flag
                    matrix[0][col] = 0
                    matrix[row][0] = 0

        
        for row in range(ROWS - 1, -1, -1):
            for col in range(COLS - 1, 0, -1):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0

        if zeroInFirstCol:
            for row in range(ROWS):
                matrix[row][0] = 0
            

                





