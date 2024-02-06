// Naive solution
// Time Complexity: O(n * log n);
// Space Complexity: O(1);
// TIME LIMIT EXCEEDED
const fn = (nums, k) => {
  const stack = [];
  const answer = [];

  for(let i = 0; i < nums.length; i++) {
    const curr = nums[i];

    stack.push(curr);
    stack.sort((a,b) => a-b);

    if(stack.length === k) {
      answer.push(stack[stack.length - 1]);

      const numToRemove = nums[i - k + 1];
      const idx = stack.indexOf(numToRemove);

      stack.splice(idx, 1);
    };

  }

  return answer;
};



/*


  nums = [1, 3, -1, -3, 5, 3, 6, 7]; k = 3;
  output = [3, 3, 5, 5, 6, 7]

  explanation:

  Window position               Max
  ---------------
  [1  3  -1] -3  5  3  6  7      3
   1 [3  -1  -3] 5  3  6  7      3
   1  3 [-1  -3  5] 3  6  7      5
   1  3  -1 [-3  5  3] 6  7      5
   1  3  -1  -3 [5  3  6] 7      6
   1  3  -1  -3  5 [3  6  7]     7
 */

const nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3;


console.log(fn(nums, k));
