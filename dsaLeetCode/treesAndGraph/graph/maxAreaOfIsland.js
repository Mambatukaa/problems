/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxAreaOfIslandII = function(grid) {
  // build graph
  const m = grid.length; // row length
  const n = grid[0].length; // column length
  const graph = new Map(); // adjacency list graph

  for(let i = 0; i < m; i++) {
    graph.set(i, []);
  };

  for(let row = 0; row < m; row++) {
    for(let column = 0; column < n; column++) {
      if(grid[row][column] === 1) {
        // add index to the graph
        graph.get(row).push(column);
      };
    };
  };

  /*
      0: 2, 7
      1: 7, 8, 9
      2: 1,2,4
      3: 1,4,5,8,10
      4: 1,4,5,8,9,10
      5: 10
      6: 7,8,9
      7: 7,8
  */

  const isValid = (row, column) => {
    if(0 > row || row >= m  || 0 > column || column >= n || grid[row][column] === 0 || visited.has(`${row},${column}`)) {
      return false;
    };

    return true
  };

  let answer = 0;
  const visited = new Set();

  const dfs = (row, column) => {
    // 0, 2
    // row, column

    let currAnswer = 0;

    if(isValid(row, column)) {
      currAnswer = 1;
      visited.add(`${row},${column}`)
      // check area
      // top
      currAnswer += dfs(row - 1, column);

      // bottom
      currAnswer += dfs(row + 1, column);

      // left
      currAnswer += dfs(row, column - 1);

      // right
      currAnswer += dfs(row, column + 1);
    };

    return currAnswer;
  };

  // call dfs on every row
  for(const [node, neighbors] of graph) {
    for(const neighbor of neighbors) {
      if(isValid(node, neighbor)) {
        answer = Math.max(answer, dfs(node, neighbor));
      };
    };
  };

  return answer;
};


/*

input: grid: []


Find max area of island

row and columns

1 - island
0 - water

horizontal or vertical.


1. Build graph

0: 2, 7
1: 7, 8, 9
2: 1,2,4
3: 1,4,5,8,10
4: 1,4,5,8,9,10
5: 10
6: 7,8,9
7: 7,8


4 directions

top 
row - 1, col

bottom
row + 1, col

left
row, col - 1

right
row, col + 1

1. Build graph
2. Declare variables (answer, visited(set))
3. Do Graph DFS. Start from row = 0, col = 2,
4. Check 4 directions and increase the curr island answer. CHECK isValid(), check isVisited
5. update answer to compare to current island answer
6. return answer
7. Time Complexity: O(n ^ 2) // building graph
8. Space Complexity: O(V + E)



*/

// Recursive
var maxAreaOfIslandIII = function(grid) {
  const m = grid.length; // row
  const n = grid[0].length; // column
  const seen = Array.from(Array(m), () => new Array(n).fill(false)); 

  const dfs = (row, column) => {
    if(row < 0 || row >= m || column < 0 || column >= n || grid[row][column] === 0 || seen[row][column]) {
      return 0;
    };

    seen[row][column] = true;

    return 1 + dfs(row - 1, column) + dfs(row + 1, column) + dfs(row, column - 1) + dfs(row, column + 1);
  };

  let answer = 0;

  for(let row = 0; row < m; row++) {
    for(let column = 0; column < n; column++) {
      answer = Math.max(dfs(row, column), answer)
    };
  }

  return answer;
};

// Iterative
var maxAreaOfIsland = function(grid) { 
  const m = grid.length; // row
  const n = grid[0].length; // column
  const seen = Array.from(Array(m), () => new Array(n).fill(false)); 

  const dfs = (row, column) => {
    const stack = [[row, column]];
    let currAnswer = 0;

    while(stack.length) {
      const [row, column] = stack.pop();

      if(row < 0 || row >= m || column < 0 || column >= n || grid[row][column] === 0 || seen[row][column]) {
        continue;
      };

      seen[row][column] = true;

      stack.push([row + 1, column])
      stack.push([row - 1, column])
      stack.push([row, column + 1])
      stack.push([row, column - 1])
      
      currAnswer++;
    };

    return currAnswer;
  };

  let answer = 0;

  for(let row = 0; row < m; row++) {
    for(let column = 0; column < n; column++) {
      if(!seen[row][column]) {
        answer = Math.max(dfs(row, column), answer)
      };
    };
  }

  return answer;
};
