// BForce, naive
// Time Complexity: O(n^2)
// Space Complexity: O(1)
const fn = (nums, k) => {

  // [x, y] === k
  // x - y = k
  // k + y = x
  
  const answer = [];
  
  for(let i = 0; i < nums.length; i++) {

    for(let j = 0; j < nums.length; j++) {

      if(i === j) {
        continue;
      }

      if(nums[i] + k === nums[j]) {
        answer.push([nums[j], nums[i]])
      };
    };

  };

  return answer;
};

// Time Complexity: O(n)
// Space Complexity: O(n)
const fnII = (nums, k) => {
  const set = new Set(nums);

  // x - k = y
  // y + k = x;

  const answer = [];

  for(const num of nums) {
    const diff = num + k;

    if(set.has(diff)) {
      answer.push([diff, num]);
    };
  }

  return answer;
};

// output: [[1,0], [0, -1], [-1, -2], [2, 1]]
const arr = [0, -1, -2, 2, 1]; 
const k = 1;

console.log(fnII(arr, k));
