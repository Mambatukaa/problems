/**
 * @param {number[][]} boxTypes
 * @param {number} truckSize
 * @return {number}
 */
 // Time Complexity: O(n * log n)
 // Space Complexity: O(n) \\ O(1)
var maximumUnits = function(boxTypes, truckSize) {
  // sort boxTypes by number of units per box
  boxTypes.sort((a, b) => b[1] - a[1]);

  let total = 0;
  
  for(const [boxCount, boxPerUnit] of boxTypes) {
    if(!truckSize) {
      break;
    };

    const taken = Math.min(boxCount, truckSize);

    total += boxPerUnit * taken;

    truckSize -= taken;
  }
      
  return total;
};


/*

input: boxTypes = [[1, 3], [2, 2], [3, 1]], truckSize = 4; // 4 box
output: 8;

maximum total number of units can be put on the truck.

1. TRY TO PUT MAX VALUE FIRST AND REDUCE THE SIZE;
2. Add the max values until truckSize reaches the limit.
3. To get max values first sort the boxTypes by number of units per box.

1. boxTypes = [[5, 10], [2, 5], [4, 7], [3,9]]
sorted = [[5, 10], [3, 9], [4, 7], [2,5]]

Put the max value until box sizes reaches the limit;

limit = 10;
total = 0;

[5, 10]
add 10, decrease boxes. [4, 10]; 9; total = 10;
add 10, decrease boxes. [3, 10]; 8; total = 20;
add 10, decrease boxes. [2, 10]; 7; total = 30;
add 10, decrease boxes. [1, 10]; 6; total = 40;
add 10, decrease boxes. [0, 10]; 5; total = 50;

limit = 5;
[3, 9]

add 9, decrease boxes. [2, 9]; 4; total = 59
add 9, decrease boxes. [1, 9]; 3; total = 68
add 9, decrease boxes. [1, 9]; 2; total = 77

limit = 2;
[4, 7] 
add 7, decrease boxes. [4, 7]; 1; total = 84
add 7, decrease boxes. [4, 7]; 0; total = 91




*/
