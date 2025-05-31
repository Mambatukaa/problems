""""
You are given an n x n integer matrix board where the cells are labeled from 1 to n2 in a Boustrophedon style starting from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.

You start on square 1 of the board. In each move, starting from square curr, do the following:

Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n2)].
This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations, regardless of the size of the board.
If next has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to next.
The game ends when you reach the square n2.
A board square on row r and column c has a snake or ladder if board[r][c] != -1. The destination of that snake or ladder is board[r][c]. Squares 1 and n2 are not the starting points of any snake or ladder.

Note that you only take a snake or ladder at most once per dice roll. If the destination to a snake or ladder is the start of another snake or ladder, you do not follow the subsequent snake or ladder.

For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination square is 2. You follow the ladder to square 3, but do not follow the subsequent ladder to 4.
Return the least number of dice rolls required to reach the square n2. If it is not possible to reach the square, return -1.

 

Example 1:


Input: board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
Output: 4
Explanation: 
In the beginning, you start at square 1 (at row 5, column 0).
You decide to move to square 2 and must take the ladder to square 15.
You then decide to move to square 17 and must take the snake to square 13.
You then decide to move to square 14 and must take the ladder to square 35.
You then decide to move to square 36, ending the game.
This is the lowest possible number of moves to reach the last square, so return 4.
Example 2:

Input: board = [[-1,-1],[-1,3]]
Output: 1
 

Constraints:

n == board.length == board[i].length
2 <= n <= 20
board[i][j] is either -1 or in the range [1, n2].
The squares labeled 1 and n2 are not the starting points of any snake or ladder.
"""


from collections import deque
class Solution:
    def snakesAndLadders(self, board) -> int:
        n = len(board)
        top_row = 0
        bottom_row = n - 1

        while top_row < bottom_row:
            board[top_row], board[bottom_row] = board[bottom_row], board[top_row] 

            top_row += 1
            bottom_row -= 1

        
        # bfs 
        # visit every neighbors curr + [1 to 6]
        # find neighbors row and col
        # if the neighbor jumps to the other number jump it
        


        # current position, steps
        q = deque([[1, 0]])
        visited = set()

        while q:
            curr, step = q.popleft()

            for i in range(1, 7):
                newNeighbor = curr + i

                if newNeighbor in visited:
                    continue
        
                print(newNeighbor)


                visited.add(newNeighbor)

                row = (newNeighbor - 1) // n
                col = (newNeighbor - 1) % n

                # check is row odd
                if row % 2:
                    col = n - 1 - col

                if board[row][col] == n * n:
                    return step + 1
          
                if board[row][col] == -1:
                    # add to the queue
                    q.append([newNeighbor, step + 1])
                else:
                    q.append([board[row][col], step + 1])


        return -1
        
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
class Solution:
    def snakesAndLadders(self, board) -> int:
        n = len(board)
        board.reverse()
        
        # bfs 
        # visit every neighbors curr + [1 to 6]
        # find neighbors row and col
        # if the neighbor jumps to the other number jump it

        def intToPos(newNeighbor):
            row = (newNeighbor - 1) // n
            col = (newNeighbor - 1) % n

            # check is row odd
            if row % 2:
                col = n - 1 - col

            return [row, col]


        # current position, steps
        q = deque([[1, 0]])
        visited = set()

        while q:
            curr, step = q.popleft()

            for i in range(1, 7):
                newNeighbor = curr + i

                row, col = intToPos(newNeighbor)
                if board[row][col] != -1:
                    newNeighbor = board[row][col]
                if newNeighbor == n * n:
                    return step + 1
                if newNeighbor not in visited:
                    visited.add(newNeighbor)
                    q.append([newNeighbor, step + 1])
                


        return -1

solution = Solution()
board = [
    
    
    [-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1],
    [-1,-1,-1,-1,-1,-1],

]

board = [[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,-1,-1,-1,-1,-1],[-1,35,-1,-1,13,-1],[-1,-1,-1,-1,-1,-1],[-1,15,-1,-1,-1,-1]]
board = [[-1,-1],[-1,3]]
board = [[-1,-1,-1],[-1,9,8],[-1,8,9]]

print("res:", solution.snakesAndLadders(board))