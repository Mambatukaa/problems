""""
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
    # Time Complexity: O(n * m)
    # Space Complexity: O(1)
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        COLS = len(matrix[0])
        ROWS = len(matrix)

        left = 0
        right = COLS - 1

        top = 0
        bottom = ROWS - 1

        res = []

        while left <= right and top <= bottom:
            # top left to top right
            for col in range(left, right + 1):
                res.append(matrix[top][col])

            # top right to bottom right
            for row in range(top + 1, bottom + 1):
                res.append(matrix[row][right])

            if top != bottom:
                # bottom right to bottom left
                for col in range(right - 1, left - 1, -1):
                    res.append(matrix[bottom][col])

            if left != right:
                # bottom left to top left
                for row in range(bottom - 1, top, -1):
                    res.append(matrix[row][left])

            left += 1
            right -= 1
            top += 1
            bottom -= 1


        return res


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0]) # Initial possible number of steps
        direction = 1 # Start off going right
        i, j = 0, -1
        output = []
        while m*n > 0:
            for _ in range(n): # move horizontally
                j += direction
                output.append(matrix[i][j])

            m-= 1

            for _ in range(m): # move vertically
                i += direction
                output.append(matrix[i][j])
            n-=1
            direction *= -1 # flip direction
        return output
        
