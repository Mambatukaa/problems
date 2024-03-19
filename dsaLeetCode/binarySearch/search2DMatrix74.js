/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
 // Time Complexity: O(log(m * n))
 // Space Complexity: O(1)
var searchMatrix = function(matrix, target) {
  const m = matrix.length; // row length
  const n = matrix[0].length; // column length

  let leftIdx = 0;
  let rightIdx = m * n - 1;

  while(leftIdx <= rightIdx) {
    const midIdx = Math.floor((leftIdx + rightIdx) / 2);
    const row = Math.floor(midIdx / n);
    const column = midIdx % n;
    const mid = matrix[row][column];

    if(mid === target) {
      return true;
    };

    if(mid > target) {
      // go left
      rightIdx = midIdx - 1;

    } else {
      // go right
      leftIdx = midIdx + 1;
    }

  };


  return false;

};

 // Time Complexity: O(log(m * n))
 // Space Complexity: O(1)
var searchMatrixII = function(matrix, target) {
    let row = 0;
    let cell = matrix[0].length - 1;

    while (row <= matrix.length - 1) {
        if (matrix[row][cell] === target) {
            return true;
        }
        else if(matrix[row][cell] > target) {
            cell--;
        }
        else {
            row++;
        }
    }

    return false;
}

