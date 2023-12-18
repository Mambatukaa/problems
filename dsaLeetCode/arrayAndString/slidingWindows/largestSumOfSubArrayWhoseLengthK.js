// Time Complexity: O(n)
// Space Complexity: O(1)

const fn = (nums, k) => {
  if(k > nums.length) {
    return -1;
  }

  let curr = 0;

  for(let i = 0; i < k; i++) {
    curr += nums[i];
  }

  let ans = curr;

  for(let i = k; i < nums.length; i++) {
    curr += nums[i] - nums[i - k];

    ans = Math.max(ans, curr);
  }

  return ans;
};


const nums = [1,5,6,3,7,10];
const k = 6;

console.log(fn(nums, k));
