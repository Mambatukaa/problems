

// Time Complexity: O(n)
// Space Complexity: O(n)
const isValid = (s) => {
  const stack = [];

  for(const ch of s) {
    if(ch === '{') {
      stack.push('}');
    } else if(ch === '[') {
      stack.push(']');
    } else if(ch === '(') {
      stack.push(')');
    } else {
      if(!stack.length || stack.pop() !== ch) {
        return false;
      };
    };
  }

  return !stack.length;
};

const s = "([{}])";
// const s = "(){}[]";

console.log(isValid(s));
