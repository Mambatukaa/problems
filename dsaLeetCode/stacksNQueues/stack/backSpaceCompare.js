/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */

 const buildStack = (string) => {
   const stack = [];

  for(const ch of string) {
    if(ch === "#") {
      stack.pop();
    } else {
      stack.push(ch);
    }
  };

  return stack.join("");
 };

// Space Complexity: O(n)
// Time Complexity: O(n)
var backspaceCompare = function(s, t) {
  return buildStack(s) === buildStack(t);
};

/*

sStack;
tStack;


for(const ch of s) {
  if(sStack.length && ch === "#") {
    tStack.pop();
  } else {
    tStack.push();
  }
};

for(const ch of t) {
  if(tStack.length && ch === "#") {
    tStack.pop();
  } else {
    tStack.push();
  }
};


return sStack === tStack;



*/
