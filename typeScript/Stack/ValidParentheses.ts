// 1. Push opening bracket into stack
// 2. If closing bracket comes check it if valid remove it else return invalid
// 3. At the end check stack's length



// Time Complexity: O(n)
// Space Complexity: O(n)

function validParenthesis(s: string): Boolean {
  const stack: string[] = []; 

  const map = new Map<string, string>([["(", ")"], ["{", "}"], ["[", "]"]]);


  for(let e of s) {
    if(map.get(e)) {
      stack.push(e);
    } else {

      if(!stack.length) {
        return false;
      }

      const open: string = stack.pop() || '';

      if(map.get(open) !== e) {
        return false;
      }

    }

  }

  return stack.length === 0;
}


console.log(validParenthesis("(([])){}"));
