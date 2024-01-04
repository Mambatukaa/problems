// Time Complexity: O(n)
// Space Complexity: O(n)
const fn = (nums) => {
  const numsSet = new Set(nums);
  const ans = [];
  
  for(const num of nums) {
    if(!numsSet.has(num + 1) && !numsSet.has(num - 1)) {
      ans.push(num);
    };
  };

  return ans;
};


const nums = [1, 3, 5, 6, 8]
console.log(fn(nums));
// answer = [1, 3, 8];
