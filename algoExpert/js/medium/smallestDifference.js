// Naive approach
// Space Complexity: O(1);
// Time Complexity: O(n^2);
const smallestDiff = (arrayOne, arrayTwo) => {
  const answer = [0,0];
  let diff = Number.MAX_SAFE_INTEGER;

  for(let i = 0; i < arrayOne.length; i++) {
    const curr = arrayOne[i];

    for(const num of arrayTwo) {
      const currDiff = Math.abs(curr - num);

      if(currDiff < diff) {
        answer[0] = curr;
        answer[1] = num;

        diff = currDiff;
      }

    }
  }

  return answer;
}

// Space Complexity: O(n)
// Time Complexity: O(nlog(n) * nlog(m));
const smallestDiffII = (arrayOne, arrayTwo) => {
  arrayOne.sort((a,b) => a-b);
  arrayTwo.sort((a,b) => a-b);

  let answer = [];

  let smallest = Infinity; 
  let current = Infinity; 

  let topIndex = 0;
  let bottomIndex = 0;

  while(topIndex < arrayOne.length && bottomIndex < arrayTwo.length) {
    const topNum = arrayOne[topIndex];
    const bottomNum = arrayTwo[bottomIndex];

    if(topNum > bottomNum) {
      current = topNum - bottomNum;
      bottomIndex++;
    } else if(topNum < bottomNum) {
      current = bottomNum - topNum;
      topIndex++;
    } else {
      return [topNum, bottomNum];
    }

    console.log(smallest, current);
    if(smallest > current) {
      smallest = current;

      answer = [topNum, bottomNum];
    }
  }

  return answer;
}

const arrayOne = [-1,3,5,10,20,28]; 
const arrayTwo = [15,17,26,134,135];

// []
// [1005, 1006, 1014, 1031, 1032]


console.log(smallestDiffII(arrayOne, arrayTwo)); // diff = [5,10]
