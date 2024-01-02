// Check ascii
const isEnglishLetter = (ch) => {
  let character = ch.charCodeAt(0);

  return (character > 64 && character < 91) || (character > 96 && character < 123);
};

// Time Complexity: O(n)
// Space Complexity: O(n)
const fn = (s) => {
  let l = 0;
  let r = s.length - 1;
  const arr = s.split("");

  while(l < r) {

    if(!isEnglishLetter(arr[l])) {
      l++;
      continue
    };

    if(!isEnglishLetter(arr[r])) {
      r--;
      continue;
    }

    [arr[l], arr[r]] = [arr[r], arr[l]];

    l++;
    r--;
  };

  return arr.join("");
};


// Time Complexity: O(n)
// Space Complexity: O(n)
const stack = (s) => {
  const letters = [];
  const arr = s.split("");

  let answer = "";

  for(const char of arr) {
    if(isEnglishLetter(char)) {
      letters.push(char);
    };
  };

  for(const char of arr) {
    if(isEnglishLetter(char)) {
      answer += letters.pop();
    } else {
      answer+= char;
    };
  }

  return answer;
};

const s = "F`abk";

console.log(stack(s));
