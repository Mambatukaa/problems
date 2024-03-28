/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 */
 // Time Complexity: O(n^ T/M ), where n = candidates.length, T = target, and M = min(candidates)
 // Space Complexity: O(T/M)
var combinationSum = function(candidates, target) {
  const answer = [];
  const curr = [];

  const backtracking = (sum, start) => {
    if(sum === target) {
      answer.push([...curr]);
      return;
    };

    for(let i = start; i < candidates.length; i++) {
      const candidate = candidates[i];

      if(sum + candidate <= target) {
        curr.push(candidate);

        backtracking(sum + candidate, i);

        curr.pop();
      }
    }

  };

  backtracking(0, 0);

  return answer;
};



/*

Input: candidates = [2,3,6,7], target = 7

Output: [[2,2,3], [7]]

Explanation:
  2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
  7 is a candidate, and 7 = 7.
  These are the only two combinations.


1. Use curr array to save all combinations. Track current arrays sum.
2. Use the same number many times to try to create combinations. If the combination reaches the limit create combination with next value;
3. If sum === target add the current to the answer.
4. If sum > target this will be base case and return.







*/
