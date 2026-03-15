class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # add rotten oranges to the queue
        # count the fresh orange if there is no fresh orange return True

        ROWS = len(grid)
        COLS = len(grid[0])

        fresh = 0
        q = deque([])

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == 1:
                    fresh += 1
                elif grid[row][col] == 2:
                    q.append((row, col))

        
        if fresh == 0:
            return 0

        # return them in number of minutes that must elapse until no cell has a fresh orange. If this is 
            # impossible return -1
        
        res = 0
        #              top      bot     right   left
        DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while q and fresh:
            print(fresh)
            size = len(q)

            for _ in range(size):
                row, col = q.popleft()

                for dr, dc in DIRECTIONS:
                    new_row = row + dr
                    new_col = col + dc

                    if new_row < 0 or new_row >= ROWS or new_col < 0 or new_col >= COLS or grid[new_row][new_col] != 1:
                        continue

                    fresh -= 1
                    grid[new_row][new_col] = 2
                    q.append((new_row, new_col))
            res += 1


        return res if fresh == 0 else -1


        
