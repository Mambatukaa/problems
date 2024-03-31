/**
 * @param {number} n
 * @param {number} k
 * @return {number[]}
 */
 // Time Complexity: O(2 ** n)
 // Space Complexity: O(2 ** n)
var numsSameConsecDiff = function(n, k) {
  const answer = [];

  const backtracking = (num, length) => {
    if(length === n) {
      answer.push(num);
      return;
    };

    for(let i = 0; i < 10; i++) {
      const lastDigit = num % 10;

      if(Math.abs(lastDigit - i) === k) {
        backtracking(num * 10 + i, length + 1);
      };
    };

  };

  

  for(let i = 1; i <= 9; i++) {
    backtracking(i, 1);
  };

  return answer;
}

 // Time Complexity: O()
 // Space Complexity: O()
var numsSameConsecDiffII = function(n, k) {
  const answer = [];

  const isValid = (num) => {
    return num >= 0 && num < 10;
  };

  const backtracking = (curr) => {
    if(curr.length === n) {
      answer.push(Number(curr.join("")));
      return;
    };

    const up = curr[curr.length - 1] + k;
    const down = curr[curr.length - 1] - k;

    if(isValid(up)) {
      curr.push(up)
      backtracking(curr);
      curr.pop();
    };

    if(up != down && isValid(down)) {
      curr.push(down);
      backtracking(curr);
      curr.pop();
    }
  };

  for(let i = 1; i <= 9; i++) {
    backtracking([i]);
  };

  return answer;
};



/*

digits length is n
difference between digits are k

n = 1; k = 7;

1. iterate starts from  num = 1 to 9;
2. find diff 
      // increase num
      if(num < k) {
      diff = num + k;

      } else {
        // decrease
        diff = num - k;
      }
      
      check diff is valid or not
      
      if(diff is valid) {
        add diff to the currentString
      }
*/


