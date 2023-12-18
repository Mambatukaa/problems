// Space Complexity: O(1)
// Time Complexity: O(n)
const fn = (nums, queries, limit) => {
  const prefix = [nums[0]];
  const answer = [];

  // build prefix
  for(let i = 1; i < nums.length; i++) {
    prefix[i] = nums[i] + prefix[prefix.length - 1];
  }

  // generate an answer
  for(const [firstIdx, secondIdx] of queries) {
    /*
    const first = firstIdx === 0 ? 0 : prefix[firstIdx - 1];
    const second = secondIdx === 0 ? 0 : prefix[secondIdx];
    */

    const curr = prefix[secondIdx] - prefix[firstIdx] + nums[firstIdx];

    answer.push(curr < limit);
  };

  return answer
};

const nums = [1, 6, 3, 2, 7, 2];
const queries = [ [0, 3], [2, 5], [2, 4] ];
const limit = 13;

console.log(fn(nums, queries, limit));
