// initial

 
/**
 * @param {character[][]} board
 * @return {boolean}
 */
 // 20 minutes
 // Time Complexity: O(n ^ 2) n = 9
 // Space Complexity: O(n ^ 2)
var isValidSudoku = function(board) {
  const n = board.length;

  const seenRow = new Array(9);
  const seenCol = new Array(9);
  const seenSquare = new Array(9);

  for(let i = 0; i < 9; i++) {
    seenRow[i] = new Set();
    seenCol[i] = new Set();
    seenSquare[i] = new Set();
  };

  for(let row = 0; row < n; row++) {

    for(let col = 0; col < n; col++) {
      const curr = board[row][col];

      if(curr === ".") {
        continue;
      };

      const squareIdx = Math.floor(row / 3) * 3 + Math.floor(col / 3);

      if(seenRow[row].has(curr) || seenCol[col].has(curr)
      || seenSquare[squareIdx].has(curr)
      ) {
        return false;
      };


      seenRow[row].add(curr);
      seenCol[col].add(curr);
      seenSquare[squareIdx].add(curr);

    }


  };


  return true;
}




/*

Check are filled cells valid.

VALID SUDOKU
No repetition in same row
No repetition in same column
No repetition in same window


Given board

numbers or .

1. To check duplication Set is good data structure
    We have 9 rows, 9 columns and 9 windows

CREATE DATASTRUCTURE rows, columns, windows each Arrays with 9 Sets

rows = [Set, Set, Set, Set, Set, Set, Set, Set, Set]
columns = [Set, Set, Set, Set, Set, Set, Set, Set, Set]
windows = [Set, Set, Set, Set, Set, Set, Set, Set, Set]

2. Iterate through row and columns
  Check current digit from the current ROW COLUMN WINDOWS Set it find duplicate return true otherwise continue.

  Find window using row and column. If currentRow = 8; currentColumn = 8

  currentSquare = ${row / 3},${col / 3} as a KEY

  on Array
  currentSquareIdx = ${row / 3} * 3 + ${col / 3};


*/
