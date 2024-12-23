//
// Space Complexity: O(n)
// Time Complexity: O(n)
const zeroSumSubArray = (nums) => {
  let total = 0;
  const sums = new Set();
  sums.add(0)

  for(const num of nums) {
    total += num;

    if(sums.has(total)) {
      return true;
    }

    sums.add(total);
  }

  return false;
}

const nums = [-8,-5,-3,0,1,10,4];

console.log(zeroSumSubArray(nums));
