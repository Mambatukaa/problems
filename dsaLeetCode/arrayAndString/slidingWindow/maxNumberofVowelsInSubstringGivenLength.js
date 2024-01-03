// Time Complexity: O(n)
// Space Complexity: O(1)
// Sliding window
const fn = (s, k) => {
  let l = 0;
  let counter = 0;
  let max = 0;

  for(let r = 0; r < s.length; r++) {

    if(isVowel(s[r])) {
      counter++;
    };

    if(r - l + 1 >= k) {
      max = Math.max(counter, max);

      if(max === k) {
        return max;
      };

      // shrink
      if(isVowel(s[l])) counter--;

      l++;
    };

  };

  return max;
};

const isVowel = (ch) => {
  return ['a', 'e', 'i', 'o', 'u'].includes(ch);
};

const s = "weallloveyou";
const k = 7;

console.log(fn(s, k));
