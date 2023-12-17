// Time complexity: O(n)
// Space complexity: O(1)
const isSubsequence = (s, t) => {
  let sPointer = 0;
  let tPointer = 0;

  while(sPointer < s.length && tPointer < t.length) {
    if(s[sPointer] === t[tPointer]) {
      sPointer++;
    };

     tPointer++;
  };

  return sPointer === s.length;
};

const s = 'abc';
const t = 'ahbgdc';

console.log(isSubsequence(s, t));
