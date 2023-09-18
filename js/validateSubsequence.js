
// Time Complexity: O(n)
// Space Complexity: O(1)
function isValidSubsequence(array, sequence) {
  let index = 0;

  for(let i = 0; i < array.length; i++) {
    const currNum = array[i];
    const sequenceNum = sequence[index];

    if(sequenceNum === currNum) {
      index++;
    }
  }

  return index === sequence.length;
}

// Time Complexity: O(n)
// Space Complexity: O(1)
function isValidSubsequenceII(array, sequence) { 

  for(let i = array.length - 1; i >= 0; i--) {
    if(sequence[sequence.length - 1] === array[i]) {
      sequence.pop();
    }
  }

  console.log(sequence);

  return !sequence.length;
}

console.log(isValidSubsequenceII([1,1,1,1,1], [1,1,1]));
