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


/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
// Time Complexity: O(n)
// Space Complexity: O(k)
var maxSlidingWindow = function(nums, k) {
  const queue = [];
  const answer = [];

  for(let i = 0; i < nums.length; i++) {

    // update queue by max element
    while(queue.length && nums[queue[queue.length - 1]] < nums[i]) {
      queue.pop();
    };

    queue.push(i);

    // remove old element
    if(queue[0] + k === i) {
      queue.shift();
    };

    // update an answer 
    if(i >= k - 1) {
      answer.push(nums[queue[0]]);
    };
  };


  return answer;
 
};


/*
 
 1 => [0] => 3 => [0, 1] => -1 => [2, 0, 1] => ans = [3] => -3 => 


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


   1. Brute force (TIME LIMIT EXCEEDED)

   2. Double ended queue (deque);
      a. Declare queue which store values index's by order.
      b. Declare answer which stores answer.
      c. iterate through nums
      d. while(current element) is greater than the queue's last element pop() element from queue
      e. add element to the queue
      f. remove old element
      g. add element to the answer queue[0]
      return answer;

 */

const nums = [1, 3, -1, -3, 5, 3, 6, 7], k = 3;


console.log(fn(nums, k));
