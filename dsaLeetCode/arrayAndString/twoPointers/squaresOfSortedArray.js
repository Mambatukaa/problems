const squaresOfSortedArray = (arr) => {
  const answer = new Array(arr.length).fill(0);

  let idx = answer.length - 1;
  let leftIdx = 0;
  let rightIdx = answer.length - 1;

  while(leftIdx <= rightIdx) {
    const leftSquare = Math.pow(arr[leftIdx], 2);
    const rightSquare = Math.pow(arr[rightIdx], 2);

    if(leftSquare > rightSquare) {
      answer[idx] = leftSquare;

      leftIdx++;
    } else {
      answer[idx] = rightSquare;

      rightIdx--;
    }

    idx--;
  };

  return answer;
};

const nums = [-7,-3,2,3,11]

console.log(squaresOfSortedArray(nums));
