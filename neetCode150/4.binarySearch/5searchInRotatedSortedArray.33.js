/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
 // Time Complexity: O(n)
 // Space Complexity: O(1)
 // 20 minutes
var search = function(nums, target) {
  // 1. check mid value in which half
  // 2. compare target based on the half
  // 3. Shrink the array until find the target
  // 4. If target not found return -1

  let leftIdx = 0;
  let rightIdx = nums.length - 1;

  while(leftIdx <= rightIdx) {
    const midIdx = Math.floor((leftIdx + rightIdx) / 2);

    if(nums[midIdx] === target) {
      return midIdx;
    };

    // find midNum's position
    // first half
    if(nums[leftIdx] <= nums[midIdx]) {
      // check target is in the first half
      if(nums[leftIdx] <= target && target < nums[midIdx]) {
        // go left
        rightIdx = midIdx - 1;
      } else {
        // go right
        leftIdx = midIdx + 1;
      };
    } else {
      // second half
      // check target is in the second half
      if(target > nums[midIdx] && target <= nums[rightIdx]) {
        // go right
        leftIdx = midIdx + 1;
      } else {
        rightIdx = midIdx - 1;
      }
    }
  };

  return -1;
};




/*

Example 1:

  Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 0;
  Output: 4


Example 2:
  Input: nums = [4, 5, 6, 7, 0, 1, 2], target = 3;
  Output: -1;


An algorithm must be O(log n) runtime.


Binary Search - O(log n);

               0  1  2  3  4  5  6
Input: nums = [4, 5, 6, 0, 1, 2, 3], target = 6;

               0  1  2  3  4  5  6
Input: nums = [4, 5, 6, 7, 1, 2, 3], target = 6;

leftIdx = 0; ====> 4
rightIdx = 6; ===> 3

midIdx = (0 + 6) / 2 = 3; ===> 0


1. Check array is sorted or rotated 
      if array is sorted do the simple binary search.
        leftNum < rightNum ARRAY IS ORTED
      
      if array is rotated find the position using midNum

      if(midNum === target) {
        return midIdx;
      };

      left < mid // mid is in first half
        target < mid && target > left
          // left side

        else
          // right side

      else left > mid // mid is in second half
        if(target > mid && target > right)
          // go left
        else
          // go right

*/
