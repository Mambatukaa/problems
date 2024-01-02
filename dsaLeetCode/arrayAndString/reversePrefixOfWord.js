// Space Complexity: O(1)
// Time Complexity: O(n)
const fn = (word, ch) => {
  // ['a', 'b', 'c'...]
  const arr = word.split("");

  for(let i = 0; i < arr.length; i++) {
    if(arr[i] === ch) {
      // reverse characters 0th index to ch index 0,3

      let l = 0;
      let r = i;

      while(l < r) {
        [arr[l], arr[r]] = [arr[r], arr[l]];

        l++;
        r--;
      };

      break;
    };

  };

  return arr.join("");
};

const word = "abcdefd";
const ch = "d";

console.log(fn(word, ch));


/*

  class Solution {
      public String reversePrefix(String word, char ch) {
          
          int ind = word.indexOf(ch);
          String s = word.substring(0, ind + 1);
          StringBuilder sb = new StringBuilder(s);
          s = sb.reverse().toString() + word.substring(ind + 1, word.length());
          return s;
      }
  }

 */
