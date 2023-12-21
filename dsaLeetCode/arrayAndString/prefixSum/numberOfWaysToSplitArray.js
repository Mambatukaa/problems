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


// We have improved the space complexity to O(1), which is a great improvement.
const waysToSplitArray = function(nums) {
    let ans = 0, leftSection = 0, total = 0;
    for (const num of nums) {
        total += num;
    }
    
    for (let i = 0; i < nums.length - 1; i++) {
        leftSection += nums[i];
        let rightSection = total - leftSection;
        if (leftSection >= rightSection) {
            ans++;
        }
    }
    
    return ans;
};


const nums = [0, 0];

console.log(fn(nums));
