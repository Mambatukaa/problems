// Time Complexity: O(n*2) because we need to traverse every position in the board, and each of the four check steps is an O(1)O(1)O(1) operation.
// Space Complexity: O(n*2) because in the worst-case scenario, if the board is full, we need a hash set each with size N to store all seen numbers for each of the N rows, N columns, and N boxes, respectively.
//
function isValidSudoku(board: string[][]) {
  const N = 9;

  const rows = new Array(N).fill(null).map(() => new Set());
  const cols = new Array(N).fill(null).map(() => new Set());
  const boxes = new Array(N).fill(null).map(() => new Set());

  for(let r = 0; r < N; r++) {
    for(let c = 0; c < N; c++) {
      const val = board[r][c];

      if(val === '.') {
        continue;
      }


      if(rows[r].has(val)) {
        return false;
      }

      rows[r].add(val);


      if(cols[c].has(val)) {
        return false
      }

      cols[c].add(val);

      const idx = Math.floor(r/3) * 3 + Math.floor(c / 3);
      console.log(val, '========', idx);

      if(boxes[idx].has(val)) {
        return false;
      }

      boxes[idx].add(val);
    }
  }

  return true;
}


const board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]


console.log(isValidSudoku(board));
