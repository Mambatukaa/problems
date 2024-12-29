
# Binary search
# Time Complexity: O(log (m * n))
# Space Complexity: O(1)
def search(matrix, target):
    ROWS = len(matrix)
    COLS = len(matrix[0])

    l = 0
    r = ROWS * COLS - 1

    while l <= r:
        mid = int(l + (r - l) / 2)
        row = int(mid / COLS)
        col = mid % COLS

        if matrix[row][col] == target:
            return True
        
        if matrix[row][col] < target:
            # go right
            l = mid + 1
        else:
            r = mid - 1

    return False





matrix = [
    [1, 3, 5, 7],
    [10, 11, 16, 20],
    [23, 30, 34, 60]
]

target = 0

print("res:", search(matrix, target))
