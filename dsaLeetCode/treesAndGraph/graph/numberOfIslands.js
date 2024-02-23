/**
 * @param {character[][]} grid
 * @return {number}
 */
// Time Complexity: 
// Space Complexity: 
var numIslands = function(grid) {
  let answer = 0;


  const n = grid.length;
  const m = grid[0].length;

  const isValid= (row, column) => {
    if(row < 0 || row > n - 1 || column < 0 || column > m - 1 || grid[row][column] === '0') {
      return false;
    };

    return true;
  }
  //                   right   left     bottom   top
  const directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

  const bfs = (startRow, startColumn) => {
    const queue = [[startRow, startColumn]];

    while(queue.length) {
      const [row, column] = queue.shift();

      for(const [dx, dy] of directions) {
        const nextRow = row + dx;
        const nextColumn = column + dy;

        if(isValid(nextRow, nextColumn)) { 
          grid[nextRow][nextColumn] = '0';
          queue.push([nextRow, nextColumn])
        };


      };
    };

  };

  // Time Complexity: 
  // Space Complexity: 
  const dfs = (row, column) => {
    if(!isValid(row, column)) return;

    grid[row][column] = '0';

    // top
    dfs(row - 1, column);

    // bottom
    dfs(row + 1, column);

    // left
    dfs(row, column - 1);

    // right
    dfs(row, column + 1);

  };

  // Time Complexity: 
  // Space Complexity: 
  for(let row = 0; row < grid.length; row++) {
    for(let column = 0; column < grid[0].length; column++) {
      if(grid[row][column] === '1' && isValid(row, column)) {
        answer++;
        grid[row][column] === '0';
        bfs(row, column);
      };
    };
  };

  return answer;
};



/*


Input: grid = [
  ["1","1","1","1","1"],
  ["1","1","0","1","1"],
  ["1","0","1","0","1"],
  ["1","1","0","1","1"]
];

output: 1;

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

helper(0, 0) {
  const queue = [[0, 0]]

  while(queue.length) {
    const [row, column] = queue.shift();

    visited.add(`${row}:${column}`);

    if(grid[row][column + 1] === 1) {
      queue.push([row, column + 1])
    };

    if(grid[row + 1][column] === 1) {
      queue.push([row, column + 1])
    };
  };
};

Output: 3

BUILD GRAPH

0: [0, 1]
1: [0, 1]
2: [2]
3: []
4: []

1. Visited (SET)
2. Iterate through rows
3. If element === 1 and unvisited pass to helper function
    helper function that mark areas of an element;

answer = 0;
for(let row = 0; row < grid[0].length; row++) {

  for(let column = 0; column < grid.length; column++) {
    const element = grid[row][column];

    if(element === 1 && !visited.has(`${row:column}`)) {
      answer++;
      helper(row, column);
    };

  };

};

return answer;



1. Search 1
  if 1 found
    mark areas until reach 0


*/
