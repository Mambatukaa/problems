// Time Complexity: O(n)
// Space Complexity: O(1)
const fn = (nums, k) => {
  const n = nums.length;

  const answer = new Array(n).fill(-1);

  // base case
  if(k * 2 >= n) {
    return answer;
  }

  const limit = k * 2;

  let l = 0;
  let sum = 0;
  
  for(let r = 0; r < n; r++) {
    sum += nums[r];

    while(r - l >= limit) {
      const idx = Math.floor((l + r) / 2);

      answer[idx] = Math.floor(sum / (limit + 1));

      sum -= nums[l];

      l++;
    };


  };

  return answer;
};

const nums = [7,4,3,9,1,86];
const k = 3;

console.log(fn(nums, k));
