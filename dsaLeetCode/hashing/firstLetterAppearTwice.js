// Time Complexity: O(n)
// Space Complexity: O(1) // Only english 26 letters
const fn = (s) => {
  const seen = new Set();

  for(const ch of s) {
    if(seen.has(ch)) {
      return ch;
    };

    seen.add(ch);
  };

  return -1;
};


const s = "abccbaacz";

console.log(fn(s))
