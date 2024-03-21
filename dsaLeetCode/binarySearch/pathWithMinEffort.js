/**
 * @param {number[][]} heights
 * @return {number}
 */
// Time Complexity: O(n * m * log k)
// Space Complexity: O(n * m)
var minimumEffortPath = function(heights) {
  const rowLength = heights.length;
  const colLength = heights[0].length;

  const isValid = (row, column) => {
    return row >= 0 && row < rowLength && column >= 0 && column < colLength;
  };

  //                  BOTTOM    TOP     RIGHT    LEFT
  const DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]

  const check = (effort) => {
    const seen = [];

    for (let i = 0; i < rowLength; i++) {
      seen.push(new Array(colLength).fill(false));
    };

    seen[0][0] = true;

    const queue = [[0,0]];

    while(queue.length) {
      const [currRow, currCol] = queue.shift();

      if(currRow === rowLength - 1 && currCol === colLength - 1) {
        return true;
      };

      // add neighbors
      for(const [dx, dy] of DIRECTIONS) {
        const nextRow = currRow + dx;
        const nextCol = currCol + dy;

        if(isValid(nextRow, nextCol) && !seen[nextRow][nextCol]) {

          if (Math.abs(heights[nextRow][nextCol] - heights[currRow][currCol]) <= effort) {
              queue.push([nextRow, nextCol]);
              seen[nextRow][nextCol] = true;
          };

        };

      };

    };
  };


  let left = 0;
  let right = 0;

  for(const arr of heights) {
    right = Math.max(right, Math.max(...arr));
  };


  while(left <= right) {
    let mid = Math.floor((left + right) / 2);

    if(check(mid)) {
      // go left
      right = mid - 1;

    } else {
      // go right
      left = mid + 1;
    };

  };

  return left;

};


const heights = [
  [1,2,2],
  [3,8,2],
  [5,3,5]]

console.log(minimumEffortPath(heights));


/*

Input: heights = [[1,2,2], [3,8,2], [5, 3,5]]

Output: 2

Explanation: The route of [1,3,5,3,5] has a maximum absolute difference of 2 in consecutive cells.
This is better than the route of [1,2,2,2,51, where the maximum absolute difference is 3.

1 2 2
3 8 2
5 3 5

DIRECTIONS = [ TOP, BOTTOM, LEFT, RIGHT ]

rows = 3;
columns = 3;

Starting point (0, 0) ====> Ending point (2, 2)


1. DO BFS using QUEUE
2. effort = diff(curr, curr[neighbor]);




*/
