def prisonAfterNDays(cells, n):
  for i in range(n):
    copy = cells.copy()
    
    for curr in range(1, 7):
      cells[curr] = 1 if copy[curr - 1] == copy[curr + 1] else 0

    cells[0] = 0
    cells[7] = 0

  return cells


cells = [1, 0, 0, 1, 0, 0, 1, 0]
n = 8

print("res:", prisonAfterNDays(cells, n))



"""

There are 8 prison cells in a row and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

• If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
• Otherwise, it becomes vacant.

Note that because the prison is a row, the first and the last cells in the row can't have two adjacent neighbors.

You are given an integer array cells where cells [i] = 1 if the ith cell is occupied and cells [i] = 0 if the ith cell is
vacant, and you are given an integer n .

Return the state of the prison after n days (i.e., n such changes described above).



****************************************

If current cell's left and right neighbor is the same the cell will be occupied (1).
  Otherwise becomes vacant.


"""
