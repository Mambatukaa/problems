/**
 * @param {number} num
 * @return {number}
 */
 // Time Complexity: O(n)
 // Space Complexity: O(n)
var maximum69Number  = function(num) {
  // convert to array
  // and change the first 6
  // convert to num and return;

  const arr = num.toString().split("");

  for(let i = 0; i < arr.length; i++) {
    if(arr[i] === '6') {
      arr[i] = '9';
      break;
    };
  };

  return Number(arr.join(""));
};


/*

num = 9669;

only 6 and 9.

Change only one digit and return the max number.

output: 9969

1. Find first 6 and replace to 9;
2. Return answer;


*/
