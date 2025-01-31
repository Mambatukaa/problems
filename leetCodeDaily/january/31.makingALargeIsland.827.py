""""
You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.
Return the size of the largest island in grid after applying this operation.
An island is a 4-directionally connected group of 1s.

Example 1:
    Input: grid = [1,0],[0,1]]
    Output: 3
    Explanation: Change one O to 1 and connect two 1s, then we get an island with area =
    3.


Example 2:

    Input: grid = [[1,1],[1,0]]
    Output: 4
    Explanation: Change the 0 to 1 and make the island bigger, only one island with area
    = 4.


Constraints:
• n == grid.length
• n == grid[i].length
• 1 < n <= 500
• grid[i][j] is either 0 or 1.
"""
class Solution:
    # Brute force 
    # Time limit exceeded
    # Time Complexity: O(v + e * n)
    # Space Complexity: O(v + e)
    def largestIsland(self, grid) -> int:
        n = len(grid)
        zerosCount = 0

        def dfs(r, c):
            if r < 0 or c < 0 or r >= n or c >= n or grid[r][c] == 0 or (r, c) in visited:
                return
            
            visited.add((r, c))

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        res = 0
        visited = set()
        for r in range(n):
            for c in range(n):
                visited = set()

                if grid[r][c] == 0:
                    grid[r][c] = 1
                    dfs(r, c)
                    grid[r][c] = 0
                    zerosCount += 1

                res = max(res, len(visited))

        return n * n if zerosCount == 0 else res

    def largestIslandII(self, grid):
        n = len(grid)
        area = {}
        areaSum = {}

        visited = set()

        def dfs(r, c):
            if r < 0 or c < 0 or r >= n or c >= n or grid[r][c] == 0 or (r, c) in visited:
                return 0

            visited.add((r, c))

            area[(r, c)] = currArea
            
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)
                
        
        currArea = 1
        zerosCount = 0
        for r in range(n):
            for c in range(n):
                # calculate the area
                if grid[r][c] == 1 and (r,c) not in visited:
                    nodesCount = dfs(r, c)

                    areaSum[currArea] = nodesCount
                    currArea += 1
                elif grid[r][c] == 0:
                    zerosCount += 1

        # edge case
        if zerosCount:
            return n * n

        res = 0

        DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        seenArea = set()

        print(area)
        print(areaSum)

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    total = 1
                    # check neighbors and get the areaSum
                    for dy, dx in DIRECTIONS:
                        newRow = dy + r
                        newCol = dx + c

                        if newRow < 0 or newCol < 0 or newRow >= n or newCol >= n or grid[newRow][newCol] == 0:
                            continue
                        
                        areaNumber = area[(newRow, newCol)]
                        
                        if areaNumber not in seenArea:
                            seenArea.add(areaNumber)
                            total += areaSum[areaNumber]

                        res = max(total, res)
                    seenArea.clear()

        return res



solution = Solution()

grid = [ 
    [0, 0, 0, 0],
    [0, 1, 1, 1],
    [1, 0, 1, 1],
    [0, 1, 1, 1]
]

grid = [[1,0],[0,1]]
print("res:", solution.largestIslandII(grid))


        
