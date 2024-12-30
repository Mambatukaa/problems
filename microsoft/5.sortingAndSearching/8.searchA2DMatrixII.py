

# Search space reduction
#Because the rows and columns of the matrix are sorted (from left-to-right and
#top-to-bottom, respectively), we can prune O(m) or
#O(n) elements when looking at any particular value.
# Time Complexity: O(m) or O(n)
# Space Complexity: O(1)
def search(matrix, target):
    ROWS = len(matrix)
    COLS = len(matrix[0])

    r = ROWS - 1
    c = 0

    while c < COLS and r >= 0:
        currVal = matrix[r][c]

        if currVal == target:
            return True
        elif currVal > target:
            # go top
            r -= 1
        else:
            c += 1
            
    return False

matrix = [ [-5]]
target = -10

print("res:", search(matrix, target))
