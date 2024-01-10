// Time Complexity: O(n + m)
// Space Complexity: O(1) , k = fixed 26
const fn = (text, pattern) => {
  const freqInText = new Array(26).fill(0);
  const freqInPattern = new Array(26).fill(0);

  const aCharCode = "a".charCodeAt(0)

  for(let i = 0; i < pattern.length; i++) {
    freqInPattern[pattern.charCodeAt(i) - aCharCode]++;
  };

  for(let i = 0; i < text.length; i++) {
    freqInText[text.charCodeAt(i) - aCharCode]++;
  };

  let answer = Infinity;

  for(let i = 0; i < 26; i++) {
    if(freqInPattern[i] > 0) {
      answer = Math.floor(Math.min(answer, freqInText[i] / freqInPattern[i]));
    };

  };

  return answer;
};


const text = "balon"
const pattern = "balloon";

console.log(fn(text, pattern));
