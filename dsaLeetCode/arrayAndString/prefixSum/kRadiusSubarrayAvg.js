// Time Complexity: O(n)
// Space Complexity: O(1)
const fn = (nums, k) => {

  if(k === 0) {
    return nums;
  };

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


// Time Complexity: O(n)
// Space Complexity: O(n)
const prefixSum = (nums, k) => {
  if(k === 0) {
    return nums;
  };

  const n = nums.length;
  const averages = new Array(n).fill(-1);

  if(k * 2 + 1 > n) {
    return averages;
  };

  const prefixSum = new Array(n + 1).fill(0);

  // generate a prefixSum
  for(let i = 0; i < nums.length; i++) {
    prefixSum[i + 1] = prefixSum[i] + nums[i];
  };

  // find averages
  for(let idx = k; idx < n - k; idx++) {
    const leftBound = idx - k;
    const rightBound = idx + k;

    const subArraySum = prefixSum[rightBound + 1] - prefixSum[leftBound];
    const average = Math.floor(subArraySum / (k * 2 + 1));

    averages[idx] = average; 
  };


  return averages;
};


const nums = [1,2,3,4,5,6];
const k = 2;

console.log(prefixSum(nums, k));
