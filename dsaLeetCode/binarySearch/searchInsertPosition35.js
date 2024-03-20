/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
 // Time Complexity: O(log n)
 // Space Complexity: O(1)
var searchInsert = function(nums, target) {
  let leftIdx = 0;
  let rightIdx = nums.length - 1;

  while(leftIdx <= rightIdx) {
    const midIdx = Math.floor((leftIdx + rightIdx) / 2);
    const mid = nums[midIdx];

    if(mid === target) {
      return midIdx;
    };

    if(mid < target) {
      // go right
      leftIdx = midIdx + 1;
    } else {
      // go left
      rightIdx = midIdx - 1;
    };
  };
    

  return leftIdx;
};


/*

nums (sorted) = [1, 3, 5, 6]; target = 5

find insert position

1. Naive approach
    compare every element with target and find right position. TC: O(n)

2. Brute force

  compare mid element with target and update element using left and right pointer;

  if(mid === target)
    return midIdx;

  if(mid < target)
    go right
    left = mid + 1;
  else  
    go left
    right = mid - 1;

  target = 5

   l  m     r
   0  1     3
  [1, 3, 5, 6]  

  compare mid with target. 3 < 5
  go right


         l  r
         2  3
  [1, 3, 5, 6]  

  (2 + 3) / 2 === 2

  return 2;
  
*************************

 target = 2

         l  m     r
         0  1     3
 nums = [1, 3, 5, 6];



 target < mid
 // go left

         r
         l       
         0       
 nums = [1, 3, 5, 6];

 mid = 0 + 0 / 2  = 0;

 1 < target
 // go right


 l = 1;
 r = 0

 iteration ends 

 return left;

*/
