/*
    Input: nums = [1,2,3]
    Output: [[1,2,3], [1,3,21, [2,1,3], [2,3,1], [3, 1,21, [3,2,1]];
 */

// Time Complextiy: O(n^2 * n!)
// Space Complextiy: O()
const permute = (nums) => {
  const answer = [];

  const backtrack = (curr) => {
    if(curr.length === nums.length) {
      answer.push([...curr]);
      return;
    };

    for(const num of nums) {
      if(!curr.includes(num)) {

        curr.push(num);
        backtrack(curr);
        curr.pop();
      };
    };
  };

  backtrack([]);

  return answer;
};

const nums = [1,2,3];

console.log(permute(nums));

/*

  1 => [1] => backtrack([1]) => [1,2] => backtrack([1,2]) => [1,2,3] => backtrack([1,2,3]) => n === m RETURN => [1,2,3] ====> 
  curr.pop() => [1,2] iteration ends ===> pop() [1, 3] ===> backtrack([1,3]) ===> [1,3,2] ===> backtrack([1,3,2]) ====> m === n RETURN => [1,3,2];
  curr.pop() => [1,3] iterationed ends ===> [1] ===> iteration ends [] ===> 2 iteration add 2 => [2] do the same things again
 

 backtrack([1,2]) iteration ends
 backtrack([1])
 
 */
