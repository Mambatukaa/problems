// Time Complexity: O(n)
// Space Complexity: O(1)
const fn = (target, nums) => {
  let min = Infinity;
  let currSum = 0;
  let l = 0;

  for(let r = 0; r < nums.length; r++) {
    currSum += nums[r];

    // shrink the window
    while(currSum >= target) {
      min = Math.min(min, r - l + 1);

      currSum -= nums[l];
      l++;
    };
  };

  return min === Infinity ? 0 : min;
};


const target = 7;
const nums = [2,3,1,2,4,3];

console.log(fn(target, nums));
