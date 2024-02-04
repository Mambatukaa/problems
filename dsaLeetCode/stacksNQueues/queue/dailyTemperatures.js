/**
 * @param {number[]} temperatures
 * @return {number[]}
 */
  // Time Complexity: O(n)
  // Space Complexity: O(n)
  // Monotonic stack
var dailyTemperatures = function(temperatures) {
  const answer = new Array(temperatures.length).fill(0);
  const stack = [];

  for(let i = 0; i < temperatures.length; i++) {
    const curr = temperatures[i];

    while(temperatures[stack[stack.length - 1]] < curr) {
      const idx = stack.pop();
      answer[idx] = i - idx;
    }; 

    stack.push(i);
  }

  /*
  true  
    add to the stack
  false
    remove from stack and update answer

  */

  return answer;
};



/*
brute force (Time Limit exceeded)
  Time Complexity: O(n^2)

[73,74,75,71,69,72,76,73]

[1, 1, 4, 2, 1, 1, 0, 0]

stack = [73] => stack[last]: 73 > curr: 74 => remove from stack and update answer => [] ans[i] = currIdx - lastIdx

 true  
  add to the stack
  false
    remove from stack and update answer

*/


