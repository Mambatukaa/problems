/**
 * @param {number[]} stones
 * @return {number}
 */
// Time Complexity: O(n * n log n)
// Space Complexity: O(1)
var lastStoneWeight = function(stones) {
  // max heap    

  while(stones.length > 1) {
    stones.sort((a, b) => b - a);
    const n = stones.length;
    let y = stones[0];
    let x = stones[1];

    if(x === y) {
      stones.shift();
      stones.shift();
    } else {
      const diff = y - x;
      stones.shift();
      stones[0] = diff;
    }
  }

  return stones[0] || 0;
};


/*

1. get 2 [x,y] max stone from stones
2. compare [x,y] 
   if x === y
      remove both from an stones
   else update y = y - x  and remove x
3. do this process until one stone left
4. return last stone






*/
