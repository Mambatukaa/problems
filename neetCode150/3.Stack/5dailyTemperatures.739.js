/**
 * @param {number[]} temperatures
 * @return {number[]}
 */
 // Time Complexity: O(n)
 // Space Complexity: O(n)
var dailyTemperatures = function(temperatures) {
  const n = temperatures.length;
  const res = new Array(n).fill(0);
  const stack = [0];

  for(let i = 1; i < n; i++) {
    const curr = temperatures[i];

    // while curr > last element of stack update the answer by index difference
    // and remove the element from stack
    while(curr > temperatures[stack[stack.length - 1]]) {
      const idx = stack.pop();
      res[idx] = i - idx;
    };

    stack.push(i);
  }

  return res;
};



/*
Brute force. 
  Time Complexity: O(n^2)
  Space Complexity: O(n)

Stack
  Iterate through array


  Hold element until Greater element comes

  [5,4,3,2,10]


  10 // 0
  2 < 10 // 1
  3 < 10 // 2
  4 < 10 // 3
  5 < 10 // 4

*/
