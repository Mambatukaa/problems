// Space Complexity: O(1)
// Time Complexity: O(n)
const fn = (nums, k) => {
  // current sum tracker
  let curr = 0;

  // build first window
  for(let i = 0; i < k; i++) {
    curr += nums[i];
  };


  let answer = curr;

  // find max window
  for(let i = k; i < nums.length; i++) {
    // update current window size using remove left element and add new right element
    curr += nums[i] - nums[i - k];

    // update answer
    answer = Math.max(curr, answer);
  };

  return answer / k;
};

const nums = [1, 12, -5, -6, 50, 3];
const k = 4;

console.log(fn(nums, k));


/*
Constraints:
  n == nums.length
  1 <= k <= n <= 10^5
  -10^4 <= nums[i] <= 10^4
 */
