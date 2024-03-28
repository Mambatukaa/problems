/**
 * @param {string} digits
 * @return {string[]}
 */
 // Time Complexity: O(4^N * N) where N is the length of digits.
 // Space Complexity: O(N)
var letterCombinations = function(digits) {
  if(!digits) {
    return []
  };
  
  const digitsMap = {
    2: ["a", "b", "c"],
    3: ["d", "e", "f"],
    4: ["g", "h", "i"],
    5: ["j", "k", "l"],
    6: ["m", "n", "o"],
    7: ["p", "q", "r", "s"],
    8: ["t", "u", "v"],
    9: ["w", "x", "y", "z"],
  };

  const answer = [];
  digits = digits.split("");
    
  const backtracking = (curr, idx) => {
    if(curr.length === digits.length) {
      answer.push(curr.join(""));

      return;
    };

    for(let i = idx; i < digits.length; i++) {
      const digit = digits[i];
      const letters = digitsMap[digit];

      for(const letter of letters) {
        curr.push(letter);

        backtracking(curr, i + 1);

        curr.pop();
      };

    };

  };


  backtracking([], 0);

  return answer;
};


/*

CREATE all possible letter combinations that the number could present.

Example 1:
  Input: digits = "23"
  Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

Example 2:
  Input: digits = "2"
  Output: ["a", "b", "c"]

Example 3:
  Input: digits = "234"




*************************
1. Create map with digit and letters.
2. Check all possible values starts from first digit.
3. When current reaches the limit add to the answer. limit = digit.length;
4. USE BACKTRACKING to track all possible combinations.


*/
