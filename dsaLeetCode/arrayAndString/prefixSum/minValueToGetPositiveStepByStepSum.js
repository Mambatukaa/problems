// Time Complexity: O(n)
// Space Complexity: O(1)
const fn = (nums) => {
  let minValue = 0;
  let total = 0;

  for(let i = 0; i < nums.length; i++) {

    total += nums[i];

    minValue = Math.min(minValue, total);

  };

  return -minValue + 1;
};

const nums = [1, -2, -3];

console.log(fn(nums));
