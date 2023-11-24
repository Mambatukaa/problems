// Time Complexity: O(n)
// Space Complexity: O(n)
const runLengthEncoding = (string) => {
  const answer = [];
  let count = 1;

  for(let i = 0; i < string.length; i++) {
    console.log(string[i], string[i + 1]);

    if(string[i] === string[i + 1]) {
      count++;
    } else {

      while(count > 9) {
        count -= 9; 
        answer.push(9 + string[i])
      }

        answer.push(count + string[i])

      count = 1;
    }
  };

  return answer.join("");
}

// Time Complexity: O(n)
// Space Complexity: O(n)
const runLengthEncodingII = (string) => {
  const answer = [];
  let count = 1;

  for(let i = 1; i < string.length; i++) {
    const prev = string[i-1];
    const curr = string[i];

    if(prev !== curr || count === 9) {
      answer.push(count + prev);

      count = 0;
    } 

     count++;
  };

  answer.push(string[string.length - 1] + count);

  return answer.join("");
}


console.log(runLengthEncodingII("AAAAAAAAAAAAAABBCCC")); //3A2B3C
