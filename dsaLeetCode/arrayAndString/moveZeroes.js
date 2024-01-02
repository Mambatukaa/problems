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

const nums = [0, 0,0, 0, 0];

console.log(fn(nums));
