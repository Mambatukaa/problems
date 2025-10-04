""""


Given an m x n matrix mat, return an array of all the elements of the array in a diagonal order.

 

Example 1:


Input: mat = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,4,7,5,3,6,8,9]
Example 2:

Input: mat = [[1,2],[3,4]]
Output: [1,2,3,4]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 104
1 <= m * n <= 104
-105 <= mat[i][j] <= 105

"""
# Time Complexity: O(n * m)
# Space Complexity: O(n * m)
class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        # up row - 1 col + 1
        # down row + 1 col -1

        direction_up = True

        res = []

        ROWS = len(mat)
        COLS = len(mat[0])

        curr_row = 0
        curr_col = 0

        while ROWS * COLS != len(res):
            if direction_up:
                while curr_row >= 0 and curr_col < COLS:
                    res.append(mat[curr_row][curr_col])
                    curr_row -= 1
                    curr_col += 1
                
                if curr_col == COLS:
                    curr_col -= 1
                    curr_row += 2
                else:
                    curr_row += 1

                direction_up = False
            else:
                while curr_col >= 0 and curr_row < ROWS:
                    res.append(mat[curr_row][curr_col])
                    curr_row += 1
                    curr_col -= 1

                if curr_row == ROWS:
                    curr_col += 2
                    curr_row -= 1
                else:
                    curr_col += 1

                direction_up = True

        return res
            
        
