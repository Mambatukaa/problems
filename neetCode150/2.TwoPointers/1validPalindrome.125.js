

// Regex
// Ascii check
// use string check to add all valid elements
// Time Complexity: O(n)
// Space Complexity: O(1)
// 10 minutes
const isPalindrome = (s) => {
  // check only non-alphanumberic characters
  
  const arr = s.toUpperCase().split("");

  const isValid = (charCode) => {
    if(48 <= charCode && charCode <= 57 || 65 <= charCode && charCode <= 90) {
      return true;
    };

    return false;
  }

  const nonAlphanumberic = [];


  for(const ch of arr) {
    // if ch in range add to the 
    // letters and numbers
    // 48 - 57 numbers
    // 65 - 90 letters
    //
    console.log(ch, ch.charCodeAt(0))
    
    if(!isValid(ch.charCodeAt(0))) {
      continue;
    };

    nonAlphanumberic.push(ch);
  };

  let left = 0;
  let right = nonAlphanumberic.length - 1;

  console.log(nonAlphanumberic)

  while(left <= right) {
    if(nonAlphanumberic[left] !== nonAlphanumberic[right]) {
      return false;
    };

    left++;
    right--;
  };
  
  return true;

};

const alphanumeric = "abcdefghijklmnopqrstuvwxyz0123456789";

const isPalindromeII = (s) => {

  const filtered = s.toLowerCase().split("").filter(c => alphanumeric.includes(c));

  let leftIdx = 0;
  let rightIdx = filtered.length - 1;

  while(leftIdx <= rightIdx) {
    if(filtered[leftIdx] !== filtered[rightIdx]) {
      return false;
    };

    leftIdx++;
    rightIdx--;
  }

  return true;

};


console.log(isPalindromeII("11A man, a plan, a canal: Panama11"));
