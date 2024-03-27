/**
 * @param {number} n
 * @param {number} k
 * @return {number[][]}
 */
// Time Complexity: O(k * n! / n - k!)
// Space Complexity: O(k)
var combine = function(n, k) {
  const answer = [];

  const backTracking = (curr, idx) => {
    // base case
    if(curr.length >= k) {
      answer.push([...curr]);
      return;
    };

    for(let i = idx; i <= n; i++) {
      curr.push(i);

      backTracking(curr, i + 1);

      curr.pop();
    };

  };


  backTracking([], 1);


  return answer;
};


/*

1 to n
k numbers of combinations

Input: n = 4, k= 2
Output : ([1,2], [1,3], [1,4], [2,3], [2,4], [3,4]
Explanation: There are 4 choose 2 = 6 total combinations.
 Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to be the same combination.

**********************************
The combination will we subset

BACKTRACKING

1. Create an array that 1 to n;
2. Create k combination starts from the first num.

n = 4; arr = [1,2,3,4]
k = 2;

use curr = [] to create combination. Once curr reaches the k limit add to the answer. And return. BASE CASE





*/
