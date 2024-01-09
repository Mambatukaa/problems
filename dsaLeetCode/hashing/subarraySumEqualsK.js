/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var subarraySum = function(nums, k) {
  const map = new Map();
  map.set(0, 1);
  
  let curr = 0;
  let ans = 0;

  for(const num of nums) {
    curr += num;
    ans += map.get(curr - k) || 0;

    map.set(curr, (map.get(curr) || 0) + 1);
  };

  console.log(map)

  return ans;
};


/*
nums = [1,2,1,2,1] k = 3 =>  [1,2], [2,1], [2,1] total subarrays equal 3;
output: 3

k = 3;
nums:
[1, 2, 1, 2, 1]

prefix:
[1, 3, 4, 6, 7];


[ -1, -1, 1 ] k = 0
[ -1, -2, -1 ]
*/

const nums = [-1, -1, 1]

console.log(subarraySum(nums, 0));
