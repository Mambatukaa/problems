/**
 * @param {number[][]} grid
 * @param {number} k
 * @return {number}
 */
// Time Complexity: O(n^2)
// Space Complexity: O(n^2)
var shortestPath = function(grid, k) {
  // row length
  const m = grid.length;
  // column length
  const n = grid[0].length;

  const isValid = (row, column) => {
    return (row >= 0 && row < m && column >= 0 && column < n); 
  };

  //                    UP      DOWN     LEFT    RIGHT
  const DIRECTIONS = [[-1, 0], [1, 0], [0, -1], [0, 1]];

  const visited = new Set();
  // row, column, remains
  visited.add(`${0},${0},${k}`);

  // row, column, remains, steps
  const queue = [[0, 0, k, 0]];

  while(queue.length) {
    const [currRow, currColumn, currRemain, steps] = queue.shift();
    
    // add neighbors
    if(currRow === m - 1 && currColumn === n - 1) {
      return steps;
    };

    for(const [dy, dx] of DIRECTIONS) {
      const newRow = currRow + dy;
      const newCol = currColumn + dx;

      if(isValid(newRow, newCol)) {
        if(grid[newRow][newCol] === 0) {
          if(!visited.has(`${newRow},${newCol},${currRemain}`)) {
            queue.push([newRow, newCol, currRemain, steps + 1])
            visited.add(`${newRow},${newCol},${currRemain}`);
          }

        } else if(currRemain && !visited.has(`${newRow},${newCol},${currRemain - 1}`)) {
            queue.push([newRow, newCol, currRemain - 1, steps + 1])
            visited.add(`${newRow},${newCol},${currRemain - 1}`);
        };

      };
    };
  };
  

  return -1;
      
};
  


/*
    steps = 0

     0 1 2

  0: 0 0 0
  1: 1 1 0
  2: 0 0 0

queue = [[0, 0, 1]]
-------> 0, 0, 1 add neighbors steps = 1
          right       bottom    
queue = [[0, 1, 1], [1, 0, 0]
-------> 0, 1, 1 steps = 2
                     bottom      right
queue = [[1, 0, 0], [1, 1, 0], [0, 2, 1]]
-------> 1, 0, 0 steps = 3
                                  bottom
queue = [[1, 1, 0], [0, 2, 1], [2, 0, 0]];
-------> 1, 1, 0 steps = 4
                                 bottom     right
queue = [[0, 2, 1], [2, 0, 0], [2, 1, 0], [1, 2, 0]]
-------> 0, 2, 1 steps = 5

queue = [[2, 0, 0], [2, 1, 0], [1, 2, 0]]

-------> 2, 0, 0 steps = 6

queue = [[2, 1, 0], [1, 2, 0]]

-------> [2,1,0] steps = 7



row 0 0 1
col 0 1 0
val 0 0 1
rem 1 1 0

---------------------------
remain = 1

[0,0] adding neighbors

[0,1] === 1 decrease remain by 1 => remain = 0;

1. [[row, column, currentRemain]]
2. Visited
3. if remain reaches limit don't add neighbors currentRemain < 0
4. else add neighbors with substracted currentRemain
5. check is node reaches the end 
    if true return level
6. Track levels to track an answer








currentRemain

0 1 0
0 1 1
1 0 0

---------------------------

** Starting queue
queue = [[0, 0, 2]];

const [row, column, currentRemain] = queue.shift();

// add neighbors





[0,0],
[1,0],
[1,0],
[1,0],
[1,0],
[1,0],
[0,0],
[0,1],
[0,1],
[0,1],
[0,0],
[1,0],
[1,0],
[0,0]


*/
