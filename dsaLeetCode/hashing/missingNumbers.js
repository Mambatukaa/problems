/**
 * @param {number[]} nums
 * @return {number}
 */
 // naive sort the array [0,1,3];
 // i'm gonna loop through array from 0 to array.length
 // i'm gonna compare current idx to the current number
 // if it's not matched i'm gonna return the idx
 // after the iteration I'm gonna return the arrays.length
 // time complexity: O(nlogn)
 // Sc: O(1)

 // 1. I'm gonna iterate through nums and I'm gonna register all numbers in my set
 // 2. I'm gonna iterate through nums started from 0 idx
 // 3. I'm gonna check idx from the set
 // 4. TC: O(n)
 // 5. SC: O(n)

// Time Complexity: O(n logn)
// Space Complexity: O(1) 
var missingNumber = function(nums) {
    nums.sort((a, b) => a - b);

    for(let i = 0; i < nums.length; i++) {
        if(i !== nums[i]) {
            return i;
        }
    };

    return nums.length;
};


 // Time Complexity: O(n)
 // Space Complexity: O(n)
 var missingNumberII = function(nums) {
    const seen = new Set(nums);

    for(let i = 0; i < nums.length; i++) {
        if(!seen.has(i)) {
            return i;
        }
    };

    return nums.length;
 };


 // Time Complexity: O(n)
 // Space Complexity: O(1)
 // Gauss' Formula
var missingNumberIII = function(nums) {
  const expectedSum = nums.length * (nums.length + 1) / 2;

  let actualSum = 0;

  for(const num of nums) {
    actualSum += num;
  };

  return expectedSum - actualSum;
};


console.log(missingNumberIII([0,1,2,3,4]))
