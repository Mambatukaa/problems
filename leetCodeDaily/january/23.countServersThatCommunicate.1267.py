""""


You are given a map of a server center, represented as a m * n integer matrix grid, where 1 means that on that
cell there is a server and 0 means that it is no server. Two servers are said to communicate if they are on the
same row or on the same column.

Return the number of servers that communicate with any other server.



Input: grid = [[1,1,0,01,10,0,1,01,[0,0,1,01,10,0,0,111
Output: 4

Explanation: The two servers in the first row can communicate with each other. The
    two servers in the third column can communicate with each other. The server at right
    bottom corner can't communicate with any other server.

"""

# Time Complexity: O(n * m)
# Space Complexity: O(n + m)
class Solution:
    def countServers(self, grid):
        # count servers
        rowsCount = {}
        colsCount = {}

        ROWS = len(grid)
        COLS = len(grid[0])

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    if r not in rowsCount:
                        rowsCount[r] = 0
                    if c not in colsCount:
                        colsCount[c] = 0
                    rowsCount[r] += 1
                    colsCount[c] += 1

        res = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    if rowsCount[r] > 1 or colsCount[c] > 1:
                        res += 1

        return res

    # Time Complexity: O(n * m)
    # Space Complexity: O(n + m)
    # Array
    def countServersII(self, grid):

        ROWS = len(grid)
        COLS = len(grid[0])

        # count servers
        rowsCount = [0] * ROWS 
        colsCount = [0] * COLS

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    rowsCount[r] += 1
                    colsCount[c] += 1

        res = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    if rowsCount[r] > 1 or colsCount[c] > 1:
                        res += 1

        return res
        
    # Time Complexity: O(n * m)
    # Space Complexity: O(1)
    def countServersIII(self, grid):
        ROWS = len(grid)
        COLS = len(grid[0])

        res = 0

        for r in range(ROWS):
            rowSum = sum(grid[r])
            if rowSum <= 1:
                # Dont mark
                continue
            
            res += rowSum

            for c in range(COLS):
                if grid[r][c]:
                    # mark
                    grid[r][c] = -1

        for c in range(COLS):
            colSum = 0
            unMarked = 0

            for r in range(ROWS):
                colSum += abs(grid[r][c])

                if grid[r][c] > 0:
                    unMarked += 1
                elif grid[r][c] < 0:
                    # mark but unnecessary
                    grid[r][c] = 1

            if colSum >= 2:
                res += unMarked

        return res

    # optimized Loops
    def countServersIV(self, grid) -> int:
        communicable_servers_count = 0
        row_counts = [0] * len(grid[0])
        last_server_in_col = [-1] * len(grid)

        # First pass to count servers in each row and column
        for row in range(len(grid)):
            server_count_in_row = 0
            for col in range(len(grid[0])):
                if grid[row][col]:
                    server_count_in_row += 1
                    row_counts[col] += 1
                    last_server_in_col[row] = col

            # If there is more than one server in the row, increase the count
            if server_count_in_row != 1:
                communicable_servers_count += server_count_in_row
                last_server_in_col[row] = -1

        # Second pass to check if servers can communicate
        for row in range(len(grid)):
            if (
                last_server_in_col[row] != -1
                and row_counts[last_server_in_col[row]] > 1
            ):
                communicable_servers_count += 1
        return communicable_servers_count
        
    

solution = Solution()


grid = [
    [1,1,0,0],
    [0,0,1,0],
    [0,0,1,0],
    [0,1,1,1]
]

print("res:", solution.countServersIII(grid))
