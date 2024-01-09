/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
// Space complexity: O(n)
// Time complexity: O(n)
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

  return ans;
};

// Brute force
// Time limit exceeded
// Time Complexity: O(n^2)
// Space Complexity: O(1)
const subarraySumBF = (nums, k) => {
  let answer = 0;
  const n = nums.length;

  for(let i = 0; i < n; i++) {
    let curr = nums[i];

    if(curr === k) {
      answer++;
    };

    for(let j = i + 1; j < n; j++) {

      curr += nums[j];

      if(curr === k) {
        answer++;
      };
    };

  };

  return answer;
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

const nums = [2,2,2,1,2,2,1,2,2,2]

console.log(subarraySumBF(nums, 2));
