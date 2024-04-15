
// Time Complexity: O(n)
// Space Complexity: O(1)
const getMinNumMoves = (blocks) => {
  const n = blocks.length;

  let min = Infinity;
  let max = -Infinity;

  let minIdx = -1;
  let maxIdx = -1;

  for(let i = 0; i < n; i++) {
    const block = blocks[i];

    if(block < min) {
      min = block
      minIdx = i;
    };

    if(block > max) {
      max = block;
      maxIdx = i;
    };
  };

  let totalSteps = n - maxIdx - 1 + minIdx;

  return minIdx > maxIdx ? totalSteps - 1 : totalSteps;
}

const blocks = [6,2,4,3,1];

console.log(getMinNumMoves(blocks))



/*

  HEAVIEST BLOCK MUST BE AT THE END
  LIGHTEST BLOCK MUST BE AT THE FIRST PLACE

  Find min moves to relocate HEAVIEST block and LIGHTEST block.....



  write a function

  getMinNumMoves(blocks)

Example 1:

  blocks = [3, 2, 1];

  1. MOVE HEAVIEST TO THE RIGHT
  
    blocks = [2, 3, 1];

  2. MOVE HEAVIEST TO THE RIGHT

    blocks = [2, 1, 3];

  3. MOVE LIGHTEST TO THE LEFT

    blocks = [1, 2, 3];

  TOTAL 3 STEPS


Example 2:

  blocks = [6, 4, 3, 1, 2];
  n = 5;



1. find indexes of min element and max element
2. Steps to locate max element n - maxIdx - 1;
3. Steps to locate minElement minIdx;
4. TotalSteps = n - maxIdx - 1 + minIdx;
5. if (minIdx > maxIdx) totalSteps - 1;

6. Return totalSteps;

 
 */
