/**
 * @param {number} n
 * @return {number}
 */
// Time Complexity: O(n!)
// Space Complexity: O(n)
var totalNQueens = function(n) {
  const backtracking = (row, diagonals, antiDiagonals, cols) => {
    if(row === n) {
      return 1;
    };

    let solutions = 0;

    for(let col = 0; col < n; col++) {
      const currDiagonal = row - col;
      const currAntiDiagonal = row + col;

      if(cols.has(col) || diagonals.has(currDiagonal) || antiDiagonals.has(currAntiDiagonal)) {
        continue;
      };

      cols.add(col);
      diagonals.add(currDiagonal);
      antiDiagonals.add(currAntiDiagonal);

      solutions += backtracking(row + 1, diagonals, antiDiagonals, cols)

      cols.delete(col);
      diagonals.delete(currDiagonal);
      antiDiagonals.delete(currAntiDiagonal);
    };

    return solutions;
  };

  return backtracking(0, new Set(), new Set(), new Set());
};


/*

*/
