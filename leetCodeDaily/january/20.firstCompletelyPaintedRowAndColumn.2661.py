""""

You are given a O-indexed integer array arr, and an m x n integer matrix mat. arr and mat both contain all
    the integers in the range [1, m * n].

Go through each index i in arr starting from index o and paint the cell in mat containing the integer arr [i].

Return the smallest index i at which either a row or a column will be completely painted in mat.



Constraints:
• m == mat. length
• n = mat [i].length
• arr. length == m * n
• 1 <= m, n <= 105
• 1 <=m * n <= 105
• 1 <= arr[il, mat[r][c] <= m * n
• All the integers of arr are unique.
• All the integers of mat are unique.


 4 3 5
 1 2 6



Example 1:

Input: arr = [1,3,4,21, mat = [|1,4], [2,3]]
Output: 2

Explanation: The moves are shown in order, and both the first row and second column
of the matrix become fully painted at arr[2].

"""


class Solution:
    # Time Complexity: O(n * m)
    # Space Complexity: O(n * m)
    def firstCompleteIndex(self, arr, mat):
        # ROWS length
        m = len(mat)
        # COLS length
        n = len(mat[0])

        seen = {}

        for r in range(m):
            for c in range(n):
                seen[mat[r][c]] = (r, c)


        ROWS = [0] * m
        COLS = [0] * n

        for i in range(len(arr)):
            [currRow, currCol] = seen[arr[i]]

            ROWS[currRow] += 1
            COLS[currCol] += 1

            if ROWS[currRow] == n or COLS[currCol] == m:
                return i

solution = Solution()

arr = [2,8,7,4,1,3,5,6,9]
mat = [[3,2,5],[1,4,6],[8,7,9]]

arr = [1,4,5,2,6,3]
mat = [[4,3,5],[1,2,6]]


print("res:", solution.firstCompleteIndex(arr, mat))

