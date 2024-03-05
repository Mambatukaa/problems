/**
 * @param {number[][]} mat
 * @return {number[][]}
 */
// Time Complexity: O(n * m)
// Space Complexity: O(n * m)
var updateMatrix = function(mat) {
  // row
  const m = mat.length;
  // column
  const n = mat[0].length;

  const answer = Array.from(Array(m), () => new Array(n).fill(0));
  const visited = Array.from(Array(m), () => new Array(n).fill(false));

  //                    top     bottom   left    right
  const directions = [[-1, 0], [1, 0], [0, -1], [0, 1]];

  const isValid = (row, column) => {
    if( row < 0 || row >= m || column < 0 || column >= n || visited[row][column]) {
      return false;
    };

    return true;
  };

  const queue = [];

  // add 0's to the queue
  for(let row = 0; row < m; row++) {
    for(let column = 0; column < n; column++) {
      if(mat[row][column] === 0) {
        visited[row][column] = true;
        queue.push([row, column]);
      };
    };
  };

  let level = 0;
  while(queue.length) {
    const size = queue.length;

    // add neighbors to the queue
    for(let i = 0; i < size; i++) {
      const [currRow, currCol] = queue.shift();

      answer[currRow][currCol] = level;

      for(const [dx, dy] of directions) {
        const newRow = currRow + dx;
        const newCol = currCol + dy;

        
        if(isValid(newRow, newCol)) {
          visited[newRow][newCol] = true;
          queue.push([newRow, newCol]);
        };
      };
    };

    level++;
  };

  console.log(answer, 'hahahhaahhahahah');

  return answer;
};



/*

// queue
row = 0, column = 0;

answer = 
0 0 0
0 1 0
1 1 1

1. Add all zeroes to the queue
2. iterate through queue add unvisited neighbors to the queue (1st level)
      replace elements by current level
3. Iterate through queue and add unvisited neighbors to the queue (2nd level)
      replace elements by current level
4. Use this logic until queue is empty. 

DO BFS






*/
