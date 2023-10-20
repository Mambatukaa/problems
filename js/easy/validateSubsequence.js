
// Time Complexity: O(n)
// Space Complexity: O(1)
function isValidSubsequence(array, sequence) {
  let index = 0;
  const n = sequence.length;

  for(let i = 0; i < array.length; i++) {
    if(index === n) {
      break;
    }

    const currNum = array[i];
    const sequenceNum = sequence[index];

    if(sequenceNum === currNum) {
      index++;
    }
  }

  return index === n;
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

// Time Complexity: O(n)
// Space Complexity: O(1)
function isValidSubsequenceIII(array, sequence) { 
  let arrIdx = 0;
  let seqIdx = 0; 

  while(arrIdx < array.length && seqIdx < sequence.length) {
    if(array[arrIdx] === sequence[seqIdx]) {
      seqIdx++;
    }

    arrIdx++;
  }

  return seqIdx === sequence.length;
}


console.log(isValidSubsequenceIII([1,1,1,1,1], [1,1,1]));
