/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
// Time Complexity: O(n * log n)
// Space Complexity: O(1) // Quick sort takes O(n)
var partitionArray = function(nums, k) {
  nums.sort((a, b) => a - b);

  let subSequence = 1;

  let currentMin = nums[0];

  for(let i = 1; i < nums.length; i++) {
    if(Math.abs(currentMin - nums[i]) > k) {
      subSequence++;
      currentMin = nums[i]
    };
  };


  return subSequence;
    
};


// start from min index
// set minElements of current sequence
// compare current element with currentMin. if (current - currentMin > k) set currentMin = current and increase the counter
// do the same thing until reach the end of an array



/*

subSequence = 1;

[1,2,3,5,6]; k = 2;

currMin = 1;

Math.abs(1 - 2) <= 2 ++++
Math.abs(1 - 3) <= 2 ++++

Math.abs(1 - 5) > 2 ----- subSequence = 1 + 1 = 2

currMin = 5

Math.abs(5 - 6) <= 2 ++++++++

end//

return subSequence = 2;


*/
