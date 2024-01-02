// Space Complexity: O(n)
// Time Complexity: O(1)
const fn = (nums) => {
  let l = 0;
  let r = 0;
  const n = nums.length;

  while(r < n) {
    const leftNum = nums[l];
    const rightNum = nums[r];

    if(leftNum !== 0) {
      l++;
    } else if(rightNum !== 0) {
      // switch
      [nums[l], nums[r]] = [nums[r], nums[l]];
      l++;
    };

    r++;
  };

  return nums;
};

const optimal = (nums) => {
  for(let curr = 0, lastNonZeroFoundAt = 0; curr < nums.length; curr++) {
    if(nums[curr] !== 0) {
      [nums[curr], nums[lastNonZeroFoundAt]] = [nums[lastNonZeroFoundAt], nums[curr]];
      lastNonZeroFoundAt++;
    };

  };

};

const nums = [1, 1, 0, 2, 0, 3];

console.log(fn(nums));
