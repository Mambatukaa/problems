/**
 * @param {number} n
 * @return {string[]}
 */
 // 30 minutes
// Time Complexity: O(?) 
// Space Complexity: O(?) 
var generateParenthesis = function(n) {
  const res = [];
  const stack = [];
  const backtracking = (left, right) => {
    if(n * 2 === stack.length) {
      res.push(stack.join(""));

      return;
    };

    if(left < n) {
      stack.push("(");
      backtracking(left + 1, right);
      stack.pop();
    };

    if(left > right) {
      stack.push(")");
      backtracking(left, right + 1);
      stack.pop();
    };
  };

  backtracking(0, 0, []);

  return res;
};


/*

n pairs of parenthesis. generate all combinations

EX 1:
  n = 3;
  "((()))", "(())()", "()(())", "()()()"


1. Generate all combinations with n opening parenthesis
2. Generate all combinations with n - 1 opening parenthesis

  Do the above steps until n reaches 0;



  Fill stack with n opeaning brackets



  (((






*/


