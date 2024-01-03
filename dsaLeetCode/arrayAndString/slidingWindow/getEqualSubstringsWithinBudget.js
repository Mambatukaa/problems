// Time Complexity: O(n)
// Space Complexity: O(1)
const fn = (s, t, maxCost) => {
  // sliding window approach
  
  let answer = 0;
  let l = 0;
  let currSum = 0;

  for(let r = 0; r < s.length; r++) {
    currSum += Math.abs(s[r].charCodeAt(0) - t[r].charCodeAt(0));

    if(currSum <= maxCost) {
      answer = Math.max(answer, r - l + 1);
    };

    while(currSum > maxCost) {
      currSum -= Math.abs(s[l].charCodeAt(0) - t[l].charCodeAt(0));
      l++;
    };
  };

  return answer;
};

const s = "abcd";
const t = "bcdf";
const maxCost = 0;

console.log(fn(s, t, maxCost));
