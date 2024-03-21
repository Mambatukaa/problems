/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
// Time Complexity: O(log n)
// Space Complexity: O(1)
var search = function(nums, target) {
  let leftIdx = 0;
  let rightIdx = nums.length - 1;

  while(leftIdx <= rightIdx) {
    const midIdx = Math.floor((leftIdx + rightIdx) / 2);
    const midNum = nums[midIdx];

    if(midNum === target) {
      return midIdx;
    };

    if(midNum > target) {
      // go to the left half
      rightIdx = midIdx - 1;
    } else {
      // go to the right half
      leftIdx = midIdx + 1;
    };

  };
    


    return -1;
};
