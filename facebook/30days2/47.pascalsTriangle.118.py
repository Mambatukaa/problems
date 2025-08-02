""""
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:


 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
Example 2:

Input: numRows = 1
Output: [[1]]
 

Constraints:

1 <= numRows <= 30
"""
# Time Complexity: O(numRows^2)
# Space Complexity: O(1) didn't count output array
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1] * row for row in range(1, numRows + 1)]
        

        print(res)
        for i in range(2, numRows):
            prev = res[i-1]
            curr = res[i]

            for j in range(1, len(curr) - 1):
                curr[j] = prev[j-1] + prev[j]

        return res


            



class Solution:
    def generate(self, num_rows: int) -> List[List[int]]:
        triangle = []

        for row_num in range(num_rows):
            # The first and last row elements are always 1.
            row = [None for _ in range(row_num + 1)]
            row[0], row[-1] = 1, 1

            # Each triangle element is equal to the sum of the elements
            # above-and-to-the-left and above-and-to-the-right.
            for j in range(1, len(row) - 1):
                row[j] = triangle[row_num - 1][j - 1] + triangle[row_num - 1][j]

            triangle.append(row)

        return triangle
