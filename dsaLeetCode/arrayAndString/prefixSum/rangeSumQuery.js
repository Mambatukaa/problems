// Time Complexity O(n)
// Space Complexity O(n)
var NumArray = function(nums) {
  const prefix = new Array(nums.length + 1).fill(0);

  for(let i = 0; i < nums.length; i++) {
    prefix[i + 1] = prefix[i] + nums[i];
  };

  this.nums = nums;
  this.prefix = prefix;
};


// Time Complexity O(1)
// Space Complexity O(1)
NumArray.prototype.sumRange = function (left, right) {
  console.log(this.prefix)
  return this.prefix[right + 1] - this.prefix[left];
};



const numArray = new NumArray([-2, 0, 3, -5, 2, -1])

console.log(numArray.sumRange(2,5))

