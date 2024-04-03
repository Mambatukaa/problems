// Time Complexity: O(n)
// Space Complexity: O(1)
var rob = function(nums) {
  if(nums.length < 2) {
    return nums[0];
  };

  const n = nums.length;

  nums[2] = nums[0] + nums[2];

  for(let i = 3; i < n; i++) {
    nums[i] = Math.max(nums[i - 2], nums[i - 3])  + nums[i];
  };

  return Math.max(nums[n - 1], nums[n - 2])
};

// Time Complexity: O(n)
// Space Complexity: O(n)
// Rob or not rob
var robII = function(nums) {
  const n = nums.length;

  const dp = new Array(n).fill(0);

  // base case
  dp[0] = nums[0];
  dp[1] = Math.max(nums[0], nums[1]);

  for(let i = 2; i < nums.length; i++) {
    dp[i] = Math.max(dp[i - 1], (dp[i - 2] + nums[i]));
  };

  return dp[n - 1];
};

var robIII = (nums) => {
  if(nums.length === 1) {
    return nums[0];
  };

  // Time Complexity: O(2^n)
  // Space Complexity: O(n)
  // Rob or not rob
  const dp = (i) => {
    if(i <= 0) {
      return nums[0];
    };

    if(i === 1) {
      return Math.max(nums[0], nums[1]);
    };
  
    // not rob or rob
    return Math.max(dp(i - 1), dp(i - 2) + nums[i]);
  };

  const n = nums.length;
  const memo = new Array(n).fill(-1);

  // Time Complexity: O(n)
  // Space Complexity: O(n)
  // Rob or not rob
  const dpWithMemo = (i) => {
    if(i === 0) {
      return nums[0];
    };

    if(i === 1) {
      return Math.max(nums[1], nums[0]);
    };

    if(memo[i] !== -1) {
      return memo[i];
    }

    // not rob || rob
    memo[i] = Math.max(dpWithMemo(i - 1), dpWithMemo(i - 2) + nums[i]);

    return memo[i];
  };

  return dpWithMemo(n - 1);};


console.log(robIII([114,117,207,117,235,82,90,67,143,146,53,108,200,91,80,223,58,170,110,236,81,90,222,160,165,195,187,199,114,235,197,187,69,129,64,214,228,78,188,67,205,94,205,169,241,202,144,240]
))
