

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

# Time complexity : O(log(n!))
# Space complexity : O(1)

def binary_search(matrix, target, start, vertical):
    lo = start
    hi = len(matrix)-1 if vertical else len(matrix[0])-1

    while hi >= lo:
        mid = int(lo + (hi - lo) / 2)
        if not vertical: # searching a row
            if matrix[start][mid] < target:
                lo = mid + 1
            elif matrix[start][mid] > target:
                hi = mid - 1
            else:
                return True
        else: # searching a column
            if matrix[mid][start] < target:
                lo = mid + 1
            elif matrix[mid][start] > target:
                hi = mid - 1
            else:
                return True

    return False

def searchMatrixBS(matrix, target):
    # an empty matrix obviously does not contain `target`
    if not matrix:
        return False

    for i in range(min(len(matrix), len(matrix[0]))):
        vertical_found = binary_search(matrix, target, i, True)
        horizontal_found = binary_search(matrix, target, i, False)

        if vertical_found or horizontal_found:
            return True
    
    return False



matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
target = 2

print("res:", searchMatrixBS(matrix, target))
