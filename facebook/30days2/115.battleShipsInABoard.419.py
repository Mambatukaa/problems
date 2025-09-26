""""
Given an m x n matrix board where each cell is a battleship 'X' or empty '.', return the number of the battleships on board.

Battleships can only be placed horizontally or vertically on board. In other words, they can only be made of the shape 1 x k (1 row, k columns) or k x 1 (k rows, 1 column), where k can be of any size. At least one horizontal or vertical cell separates between two battleships (i.e., there are no adjacent battleships).

 

Example 1:


Input: board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
Output: 2
Example 2:

Input: board = [["."]]
Output: 0
 

Constraints:

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] is either '.' or 'X'.
 

Follow up: Could you do it in one-pass, using only O(1) extra memory and without modifying the values board?







"""
# Time Complexity: O(m * n)
# Space Complexity: O(1)
class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        ROWS = len(board)
        COLS = len(board[0])

        res = 0

        # if the right side is "." and 
         
        for row in range(ROWS):
            for col in range(COLS):
                if board[row][col] == "X":
                    if row > 0 and board[row - 1][col] == "X":
                        continue
                    if col > 0 and board[row][col - 1] == "X":
                        continue
                    res += 1

        return res
        
