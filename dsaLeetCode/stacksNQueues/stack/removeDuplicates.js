 /* @param {string} s
 * @return {string}
 */
 // Space Complexity: O(n)
 // Time Complexity: O(n)
var removeDuplicates = function(s) {
  const stack = [];
  
  for(const ch of s) {
    if(!stack.length) {
      stack.push(ch);
      continue;
    };

    if(stack[stack.length - 1] === ch) {
      stack.pop();
    } else {
      stack.push(ch);
    };
  };
    
  return stack.join("");
};



/*
s = "abbaca";
output: "ca"

     1221
s = "abbaca";

      0 1 2 3 4 5
curr: a b b a c a
stack

0: a => [a]
1: b => [a] => stack.peek() => a !== b ==> stack.push(b); => stack = [a,b];
2: b => [a,b] => stack.peek() => b === b ==> stack.pop() => stack = [a];
3: a => [a] => stack.peek() => a === a ==> stack.pop() => stack = [];
4. c => [] => [c]
5. a => [c] => stack.peek() => c !== a => stack.push(a) => stack = [ca];


1. Loop through s
2. compare stack last element with ch if they are same remove from stack
  else
    add ch to the stack
4. return stack;



*/
