// Time Complexity: O(n)
// Space Complexity: O(1)
const fn = (nums) => {
  let counter = 0;
  const prefix = [nums[0]];

  // prepare prefix
  for(let i = 1; i < nums.length; i++) {
    prefix[i] = nums[i] + prefix[prefix.length - 1];
  };
  
  // solution
  const lastNum = prefix[prefix.length - 1];

  for(let i = 0; i < prefix.length - 1; i++) {
    const curr = prefix[i];

    if(lastNum - curr <= curr) {
      counter++;
    };

  };

  return counter;
};


const nums = [0, 0];

console.log(fn(nums));
