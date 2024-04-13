/**
 * @param {number[][]} matrix
 * @param {number} target
 * @return {boolean}
 */
 // Time Complexity: O(log n * m)
 // Space Complexity: O(1)
 // 8 minutes
var searchMatrix = function(matrix, target) {
  const m = matrix.length;
  const n = matrix[0].length;

  let left = 0;
  let right = m * n - 1;

  while(left <= right) {
    const midIdx = Math.floor((left + right) / 2);
    const row = Math.floor(midIdx / n); 
    const col = Math.floor(midIdx % n); 

    const mid = matrix[row][col];


    if(mid === target) {
      return true;
    };

    if(mid > target) {
      // go left
      right = midIdx - 1;
    } else {
      left = midIdx + 1;
    };

  };

return false;

    
};
