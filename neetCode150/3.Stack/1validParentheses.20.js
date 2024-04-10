/**
 * @param {string} s
 * @return {boolean}
 */
 // 6 minutes
 // Time Complexity: O(n)
 // Space Complexity: O(n)
var isValid = function(s) {
  const pairs = {
    "}": "{",
    ")": "(",
    "]": "[" 
  };
  
  const stack = [];

  for(const char of s) {
    // add opening brackets to the stack
    if(!pairs[char]) {
      stack.push(char);
    } else {
      if(pairs[char] !== stack.pop()) return false;
    };
  };

  return stack.length === 0;
};

/*

Add opening parentheses to the stack

  when closing parenthesis show up
    the last opening parentheses must be closing



*/
