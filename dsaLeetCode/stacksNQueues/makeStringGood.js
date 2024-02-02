/**
 * @param {string} s
 * @return {string}
 */
 // Time Complexity: O(n)
 // Space Complexity: O(n)
var makeGood = function(s) {
  const stack = []; //LIFO

  for(let ch of s) {
    if(!stack.length) {
      stack.push(ch);
      continue;
    }

    const lastEl = stack[stack.length - 1];

    if(ch !== lastEl) {
      // adjacent
      if(ch.toUpperCase() === lastEl.toUpperCase()) {
        stack.pop();
        continue;
      }
    }; 

    stack.push(ch);
  };


  return stack.join("");
};


/*

s = "leEeetcode";
output: "leetcode"

two adjacent character ==== s[i] and s[i+1] lower case letter and is the upper case letter

1. Use stack = []; LIFO
2. compare current character with the last element in stack
  If there are adjacent remove last element from stack
  else add current element to the stack
3. How to check is it adjacement or not
  if there are different in first comparision like. curr !== lastElement
    convert them to upperCase and compare again
    if true there are adjacent
    else they are not
  if they are the same add to the stack
4. Convert stack to string and return;

*/
