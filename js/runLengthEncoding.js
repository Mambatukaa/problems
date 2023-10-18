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


console.log(runLengthEncoding("AAAAAAAAAAAAAAAAABBCCC")); //3A2B3C
