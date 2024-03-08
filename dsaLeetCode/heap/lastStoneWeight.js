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


function heapifyHelper(arr, index) {
  const n = arr.length;
  const leftChildIdx = index * 2 + 1;
  const rightChildIdx = index * 2 + 2;
  let largestIdx = index;

  if(leftChildIdx < n && arr[leftChildIdx] > arr[largestIdx]) {
    largestIdx = leftChildIdx;
  };

  if(rightChildIdx < n && arr[rightChildIdx] > arr[largestIdx]) {
    largestIdx = rightChildIdx;
  };

  if(index !== largestIdx) {
    //swap
    [arr[index], arr[largestIdx]] = [arr[largestIdx], arr[index]];
    
    heapifyHelper(arr, largestIdx);
  };
};

function heapify(arr) {
  for(let i = Math.floor(arr.length / 2) - 1; i >= 0; i--) {
    heapifyHelper(arr, i);
  }
}

/**
 * @param {number[]} stones
 * @return {number}
 */
var lastStoneWeightII = function(stones) {
  while(stones.length > 1) {
    heapify(stones);

    console.log(stones)

    const y = stones[0];

    if(stones[1] < stones[2]) [stones[2], stones[1]] = [stones[1], stones[2]];

    const x = stones[1];

    console.log(x, '====', y)

    if(y === x) {
      stones.shift();
      stones.shift();
    } else {
      stones.shift();
      stones[0] = y - x;
    };

  };

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
