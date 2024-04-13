// initial
 /**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
 // Time Complexity: O(log n)
 // Space Complexity: O(1)
 // 5 minutes
var search = function(nums, target) {
  let left = 0;
  let right = nums.length - 1;

  while(left <= right) {
    const midIdx = Math.floor((left + right) / 2);
    const mid = nums[midIdx];

    if(mid === target) {
      return midIdx;
    };

    // go right
    if(mid < target) {
      left = midIdx + 1;
    } else {
      // go left
      right = midIdx - 1;
    };
  };

  return -1;
    
};
