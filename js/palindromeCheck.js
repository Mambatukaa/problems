// Time Complexity: O(n)
// Space Complexity: O(1)
const palindromeCheck = (string) => {
  // use two pointers
  let left = 0;
  let right = string.length - 1;

  while(left < right) {
    if(string[left] !== string[right]) {
      return false;
    }

    left++;
    right--;
  }

  return true;
}

// Time Complexity: O(n)
// Space Complexity: O(n)
const palindromeCheckII = (string, i = 0) => {
  // 2 -> 1 -> 0
  const j = string.length - 1 - i;

  return i >= j ? true : string[i] === string[j] && palindromeCheckII(string, i + 1);

}

console.log(palindromeCheckII('aba'));
