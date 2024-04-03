/*
 
 
 cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1];

 */


// Bottom up solution
// Time Complexity: O(n)
// Space Complexity: O(1)
const minCostClimbingStairs = (cost) => {
  const n = cost.length;
  
  for(let i = 2; i < n; i++) {
    cost[i] = Math.min(cost[i - 1], cost[i - 2]) + cost[i];
  };


  return Math.min(cost[n - 1], cost[n-2]);
};

// Bottom up solution
// Time Complexity: O(n)
// Space Complexity: O(n)
const minCostClimbingStairsIII = (cost) => {
  const n = cost.length;
  const dp = new Array(n + 1).fill(0);
  
  for(let i = 2; i <= n; i++) {
    dp[i] = Math.min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2]);
  };

  console.log(cost, '-------')
  console.log(dp, '========')

  return dp[n];
};


// Top-down solution
// Time Complexity: O(n)
// Space Complexity: O(n)
const minCostClimbingStairsII = (cost) => {
  const memo = new Map();

  const dp = (i) => {
    if(i <= 1) {
      return 0;
    };

    if(memo.has(i)) {
      return memo.get(i);
    }

    memo.set(i, Math.min(dp(i - 1) + cost[i - 1], dp(i - 2) + cost[i - 2]));

    return memo.get(i);
  };

  return dp(cost.length);
};

const cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1];

console.log(minCostClimbingStairsIII(cost));
