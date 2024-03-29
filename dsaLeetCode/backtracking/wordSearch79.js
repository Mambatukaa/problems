/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
// Time Complexity: O(n * m * 3^L) L = word.length
// Space Complexity: O(n * m)
var exist = function(board, word) {
  const m = board.length; // rows length;
  const n = board[0].length; // columns length

  const isValid = (row, column) => {
    return row >= 0 && row < m && column >= 0 && column < n;
  };

  //                    TOP   BOTTOM     LEFT    RIGHT
  const DIRECTIONS = [[1, 0], [-1, 0], [0, -1], [0, 1]]

  const backtracking = (row, column, seen, i) => {
    if(i === word.length) {
      return true;
    };

    for(const [dy, dx] of DIRECTIONS) {
      const newRow = row + dy;
      const newCol = column + dx;

      if(isValid(newRow, newCol) && !seen[newRow][newCol] && board[newRow][newCol] == word[i]) {
        seen[newRow][newCol] = true;
        if(backtracking( newRow, newCol, seen, i + 1)) {
          return true;
        };

        seen[newRow][newCol] = false;

    };
    };

    return false;
  };

  // find starting point
  for(let row = 0; row < m; row++) {
    for(let col = 0; col < n; col++) {
      let seen = [];

      for(let i = 0; i < m; i++) {
        seen.push(new Array(n).fill(false));
      };

      seen[row][col] = true;

      if(board[row][col] === word[0] && backtracking(row, col, seen, 1)) {
         return true;
      };

    };

  };

  return false;
};



/*
board = m x n
word = ""


Search word from board;

**************************
1. Letters are horizontally and vertically neighbors.
2. DFS - BFS (Backtracking)



*/
