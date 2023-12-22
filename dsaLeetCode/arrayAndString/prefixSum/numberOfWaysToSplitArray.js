// Time Complexity: O(n)
// Space Complexity: O(n)
const fn = (nums) => {
  let counter = 0;
  const prefix = [nums[0]];

  // prepare prefix
  for(let i = 1; i < nums.length; i++) {
    prefix[i] = nums[i] + prefix[prefix.length - 1];
  };
  
  for(let i = 0; i < prefix.length - 1; i++) {
    const leftSection = prefix[i];
    const rightSection = prefix[prefix.length - 1] - prefix[i];

    if(leftSection >= rightSection) {
      counter++;
    };

  };

  return counter;
};


// We have improved the space complexity to O(1), which is a great improvement.
// Time Complexity: O(n)
// Space Complexity: O(1)
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


const nums = [1,2,3,4,5];

console.log(fn(nums));
