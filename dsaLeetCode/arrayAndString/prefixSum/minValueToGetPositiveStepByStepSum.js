// Time Complexity: O(n)
// Space Complexity: O(1)
const fn = (nums) => {

  let minValue = nums[0];

  for(let i = 1; i < nums.length; i++) {
    nums[i] = nums[i - 1] + nums[i];

    if(nums[i] < minValue) {
      minValue = nums[i];
    }
  };

  console.log(nums)

  return minValue < 0 ? Math.abs(minValue) + 1 : minValue;
};

const nums = [2,3,4, -5, -1];

console.log(fn(nums));
