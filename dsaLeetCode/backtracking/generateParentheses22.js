/**
 * @param {number} n
 * @return {string[]}
 */
 // Brute force (TIME LIMIT EXCEEDED)
 // Time Complexity: O(2^ 2 * n * n)
 // Space Complexity: O(2^ 2 * n * n) // Catalan number
var generateParenthesisII = function(n) {
  const isValid = (curr) => {
    let leftCount = 0;

    for(const char of curr) {

      if(char === "(") {
        leftCount++;
      } else {
        leftCount--;
      }

      if(leftCount < 0) {
        return false;
      }

    };

    return leftCount === 0;

  };


  const queue = [""];
  const answer = [];

  while(queue.length) {
    const currString = queue.shift();

    if(currString.length === 2 * n) {
      if(isValid(currString)) {
        answer.push(currString);
      };

      continue;
    };

    queue.push(currString + "(")
    queue.push(currString + ")")
  };

  return answer;
}

// Time Complexity: O(4^n / √n)
// Space Complexity: O(n)
var generateParenthesis = function(n) {
  const answer = [];

  const backtracking = (curr, leftCount, rightCount) => {
    if(curr.length == n * 2) {
      answer.push([...curr].join(""))
      return;
    };

    if(leftCount < n) {
      curr.push("(");
      backtracking(curr, leftCount + 1, rightCount);
      curr.pop()
    };

    if(leftCount > rightCount) {
      curr.push(")");
      backtracking(curr, leftCount, rightCount + 1);
      curr.pop();
    };

  };

  backtracking([], 0, 0)
    
  return answer;
};

/*
n = 3;

Generate n number of valid parenthesis combinations.



*/
