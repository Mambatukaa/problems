/**
 * @param {number} k
 * @param {number} n
 * @return {number[][]}
 */
 // Time Complexity: O(9! * K / (9 - K)!)
 // Space Complexity: O(K) k = number of digits combination
var combinationSum3 = function(k, n) {
  const answer = []

  const backtracking = (curr, sum) => {
    if(sum > n) {
      return;
    };

    if(curr.length === k) {
      if(sum === n) {
        answer.push([...curr]);
      };

      return;
    };

    for(let i = (curr[curr.length - 1] || 0) + 1; i < 10; i++) {
      curr.push(i);
      backtracking(curr, sum + i);
      curr.pop();
    };
  }

  backtracking([], 0);

  return answer;
};

/*

1. 1 through 9 used
2. Each number is used at most once.

K numbers sub up to n;


input: k = 3; n = 7;
output: [[1, 2, 4]]

1 + 2 + 4 = 7;

input: k = 3, n = 9;
output: [[1, 2, 6], [1, 3, 5], [2, 3, 4]];

1 + 2 + 6 = 9;
1 + 3 + 5 = 9;
2 + 3 + 4 = 9;


****************

first level (num);
  second level (num + 1);
    third level (num + 2);



iterate through 1 to 9
  [1]

    1 + 2 + 3 = 6;
    1 + 2 + 4 = 7;
    1 + 2 + 5 = 8;
    1 + 2 + 6 = 9;
      return
    1 + 3 + 4 = 8;
    1 + 3 + 5 = 9;
      return
    1 + 4 + 5 = 10
      return

*/
