/**
 * @param {string} path
 * @return {string}
 */
// Space Complexity: O(n)
// Time Complexity: O(n)
var simplifyPath = function(path) {
  const stack = [];
  const components = path.split("/");

  for(const directory of components) {
    if(directory === "." || !directory) {
      continue;
    } else if(directory === "..") {
        stack.pop();
    } else {
      stack.push(directory);
    }
  };

  return `/${stack.join("/")}`;
    
}


/*
path: "/home/"
output: "/home"


/home/

edge case 1:
  no trailing slash after the last directory name
  multiple consecutive slashes are replaced by a single one


/a/../../.../ => /...

stack = [...]




*/


