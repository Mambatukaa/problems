"""
Given an m x n matrix, return all elements of the matrix in spiral order.

 

Example 1:


Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]
Example 2:


Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        res = []

        left = 0
        right = COLS - 1

        top = 0
        bottom = ROWS - 1

        while left <= right and top <= bottom:

            # top left --> top right
            # left
            for i in range(left, right + 1):
                res.append(matrix[top][i])
            
            # down

            # top right --> bottom right
            for i in range(top + 1, bottom + 1):
                res.append(matrix[i][right])


            # right

            # bottom right --> bottom left
            if top != bottom:
                for i in range(right - 1, left - 1, -1):
                    res.append(matrix[bottom][i])

            # up
            if left != right:
                # bottom left --> top left
                for i in range(bottom - 1, top, -1):
                    res.append(matrix[i][left])


            left += 1
            right -= 1
            top += 1
            bottom -= 1

        return res





class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        direction = 1


        res = []
        row = 0
        col = -1

        while ROWS * COLS > 0:
            # Horizontally
            for _ in range(COLS):
                col += direction
                res.append(matrix[row][col])

            ROWS -= 1
            for _ in range(ROWS):
                row += direction
                res.append(matrix[row][col])
            COLS -= 1
            direction *= -1
            print(res)
            
        return res
                

"""

L_TOP ---> R_TOP

R_TOP ---> R_BOTTOM

R_BOTTOM ---> L_BOTTOM

L_BOTTOM ---> L_TOP

"""        
