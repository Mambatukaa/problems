/**
 * @param {number[]} nums
 * @return {number[][]}
 */
// Time Complexity: O(n * 2^n) 
// Space Complexity: O(n)
var subsets = function(nums) {
  const answer = [];

  const backTrack = (nums, curr, idx) => {
    if(idx > nums.length) {
      return;
    };

    answer.push([...curr]);

    for(let i = idx; i < nums.length; i++) {
      curr.push(nums[i]);

      backTrack(nums, curr, i + 1);

      curr.pop();
    };
  };

  backTrack(nums, [], 0);

  return answer;
};
