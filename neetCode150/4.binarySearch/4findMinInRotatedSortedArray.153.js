/**
 * @param {number[]} nums
 * @return {number}
 */
// Time Complexity: O(log n)
// Space Complexity: O(1)
var findMin = function(nums) {
  let leftIdx = 0;
  let rightIdx = nums.length - 1;

  while(leftIdx <= rightIdx) {
    const midIdx = Math.floor((leftIdx + rightIdx) / 2)
    const midNum = nums[midIdx];

    const leftNum = nums[leftIdx];
    const rightNum = nums[rightIdx];

    if(leftNum <= rightNum) {
      return leftNum;
    };

    if(midNum < rightNum) {
      // to left
      rightIdx = midIdx;
    } else {
      // to right
      leftIdx = midIdx + 1;
    };

  };

};

var findMinII = function(nums) {
  let res = nums[0];
  let leftIdx = 0;
  let rightIdx = nums.length - 1;

  while(leftIdx <= rightIdx) {
    const midIdx = Math.floor((leftIdx + rightIdx) / 2)
    const midNum = nums[midIdx];

    const leftNum = nums[leftIdx];
    const rightNum = nums[rightIdx];

    if(leftNum < rightNum) {
      res = Math.min(res, leftNum);
      break;
    };

    res = Math.min(res, midNum);

    if(midNum >= leftNum) {
      // to right
      leftIdx = midIdx + 1;
      
    } else {
      // to left
      rightIdx = midIdx - 1;
    };

  };

  return res;
};


//                   L  M  R
console.log(findMin([3, 4, 2]))

/*

left, mid, right;

left > right && mid < right
  LITTLE VALUE MUST BE IN THE LEFT SIDE
  SHRINK ARRAY TO THE LEFT SIDE

left > right && mid > right
  LITTLE VALUE MUST BE IN THE RIGHT SIDE
  SHRINK ARRAY TO THE RIGHT SIDE

if(left < right) {
  return left;
};

 

[3, 4, 5, 1, 2];


left > right
 // go right
 left = mid;
right > left
  // go left
  right = mid


3 > 2
  // go right
  5 > 2
    // go right
    1 < 2
      // go left
      loop ends


[4, 5, 6, 7, 0, 1, 2]

4 > 2
  // go right
  7 > 2
    // go right
    0 < 2
    // go left
    0 < 1
    // go left

Update pointer to the min side
  At the end left pointer will be min
BINARY SEARCH




*/
