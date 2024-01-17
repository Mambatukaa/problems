/**
 * @param {number[][]} grid
 * @return {number}
 */
// Time Complexity: O(n^2)
// Space Complexity: O(n^2)
var equalPairs = function(grid) {
    const rowMaps = new Map();

    for(const row of grid) {
        const rowString = row.join(",");

        rowMaps.set(rowString, (rowMaps.get(rowString) || 0) + 1);
    };

    let answer = 0;

    for(let c = 0; c < grid.length; c++) {
        const arr = [];

        for(let r = 0; r < grid[c].length; r++) {
            arr.push(grid[r][c]);
        };

        const columnKey = arr.join(",");
        if(rowMaps.has(columnKey)) {
            // same pair found
            answer += rowMaps.get(columnKey);
        };

    };
    
    return answer;
};

const grid = [
  [3,2,1],
  [1,7,6],
  [2,7,7]
];

console.log(equalPairs(grid));

/*
            0 1 2 
grid = [ 0 [3,2,1], 
         1 [1,7,6],
         2 [2,7,7] ]

column[1] = [2,7,7]
row[2] = [2,7,7]

column[1] === row[2] => true

output: 1;

1. First approach brute force
2. If same pair found increase the counter
3. r.length === column.length
4. TC: O(r * c^2) SC: O(1)
[3,2,1]


map: {
    0: [3,2,1],
    1: [1,7,6],
    2: [2,7,7],
};

321: 1,
176: 1,
277: 1

iterate through columns convert columns array to the string. then check from the map. if found increase counter by value of the row;

TC: O(n) => join function takes O(n) 
SC: O(n)

[11,1],
[1,11]



*/
