/**
 * @param {number[][]} grid
 * @return {number}
 */
 // Time Complexity: O(n)
 // Space Complexity: O(n)
var shortestPathBinaryMatrix = function(grid) {
  const n = grid.length;

  if(!n || grid[0][0] !== 0 || grid[n-1][n-1] !== 0) {
    return -1;
  };

  /*
  0 0 0
  1 1 0
  1 1 0
  */

  const visited = Array.from(Array(n), () => new Array(n).fill(false));

  const isValid = (row, column, queue, path) => {
    if(row < 0 || row >= n || column < 0 || column >= n || visited[row][column] || grid[row][column] === 1 ) {
      return false;
    };

    visited[row][column] = true;

    queue.push([row, column, path + 1] )

    return true;
  };

  const queue = [[0, 0, 1]];

  visited[0][0] = true;

  const DIRECTIONS = [[-1, -1], [0, -1], [1, -1 ], [-1, 1], [0, 1], [1, 1], [-1, 0], [1, 0]]

  while(queue.length) {
    const [row, column, path] = queue.shift();

    if(row === n - 1 && column === n - 1 ) {
      return path;
    };

    // check neighbors
     // Left Top -- (row - 1, column - 1)
     for(const [dirRow, dirCol] of DIRECTIONS) {
       const newRow = row + dirRow;
       const newCol = column + dirCol;

      isValid(newRow, newCol, queue, path);
     };
  };

  return -1;
};



/*

Top left to bottom right cell
  All the visited cells of the path are 0
if there is no clear path return -1;
shortest clear path

m = grid.length; // rows
n = grid[0].length; // columns


top left [0][0] starting point

bottom right [m - 1][n - 1]

0 1
1 0

**** edge case
if(grid[0][0] !== 0 || grid[m - 1][n - 1] !== 0) {
  return -1;
};

n x n

Left
1. Left Top
2. Left 
3. Left Bottom
Right
1. Right Top
2. Right 
3. Right Bottom

Top
Bottom

Check 8 directions;

***** Left 
Left Top -- (row - 1, column - 1)
Left -- (row, column - 1)
Left Bottom -- (row + 1, column - 1)

***** Right
Right Top -- (row - 1, column + 1)
Right -- (row, column + 1)
Right Bottom -- (row + 1, column + 1)

**** Top, Bottom
Top - (row + 1, column)
Bottom - (row, column + 1)


// INVALID
if(row < 0 || row >= n.length || column < 0 || column >= n.length || grid[row][column] === 1 || visited()) {
  do not add to queue
};

queue = [ [row, column, length] ];


0 0 0
1 1 0
1 1 0


BFS and then Find shortest path

1. Start BFS from starting point
2. Go to the above directions
3. DO BFS 





*/

var shortestPathBinaryMatrix = function(grid) {
    const n = grid.length
    if (grid[0][0] || grid[n-1][n-1]) return -1

    const Xqueue = [0] 
    const Yqueue = [0]
    const deltaX = [-1,  0,  1,  1,  1,  0, -1, -1]
    const deltaY = [-1, -1, -1,  0,  1,  1,  1,  0]

    let count = 1, level = count, nextLevel = 0
    
    while(level) { 
        const col = Xqueue.shift()
        const row = Yqueue.shift()

        if(col === n-1 && row === n-1) return count
        
        for (let i = 0; i < 8; i++){
            const newCol = col + deltaX[i]
            const newRow = row + deltaY[i]
            
            if (newCol < 0 || newCol === n) continue
            if (newRow < 0 || newRow === n) continue
            if (grid[newRow][newCol]) continue
            
            Xqueue.push(newCol)
            Yqueue.push(newRow)
            grid[newRow][newCol] = 1
            nextLevel++
        }
        
        level--
        if (!level) {
            level = nextLevel
            nextLevel = 0
            count++
        }
    }
    return -1
}
