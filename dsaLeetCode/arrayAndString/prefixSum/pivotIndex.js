// Time Complexity: O(n)
// Space Complexity: O(1)
const fn = (nums) => {
  let total = 0;

  for(const num of nums) {
    total += num;
  };

  let leftSum = 0;

  for(let i = 0; i < nums.length; i++) {
    const rightSum = total - nums[i] - leftSum;

    if(rightSum === leftSum) {
      return i;
    };

    leftSum += nums[i];
  }

  return -1;
};


const nums = [0, 0, 2, 1, -1];

console.log(fn(nums));
