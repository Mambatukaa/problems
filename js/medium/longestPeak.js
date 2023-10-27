// Time Complexity: O(n)
// Space Complexity: O(1)
const longestPeak = (array) => {
  let longestPeak = 0;

  for(let i = 1; i < array.length - 1; i++) {
    const prev = array[i-1];
    const curr = array[i];
    const next = array[i+1];


    if(prev < curr && curr > next) {
      let counter = 3;
      let dIdx = i - 1;
      let iIdx = i + 1;

      while(dIdx > 0 && array[dIdx] > array[dIdx - 1]) {
        console.log('--')
        dIdx--;
        counter++;
      }

      while(iIdx < array.length - 1 && array[iIdx] > array[iIdx + 1]) {
        console.log('------', array[iIdx], '===', array[iIdx + 1]);
        iIdx++;
        counter++;
      }

      if(longestPeak < counter) {
        longestPeak = counter;
      }
    }

  }

  return longestPeak;
}


// Time Complexity: O(n)
// Space Complexity: O(1)
const longestPeakII = (array) => {
  let longestPeak = 0;
  let i = 1;

  while(i < array.length - 1) {
    const isPeak = array[i - 1] < array[i] && array[i] > array[i + 1];

    if(!isPeak) {
      i++;
      continue;
    }

    let leftIndex = i - 2;

    while(leftIndex >= 0 && array[leftIndex] < array[leftIndex + 1]) {
      leftIndex--;
    }

    let rightIndex = i + 2;

    while(rightIndex < array.length && array[rightIndex] < array[rightIndex - 1]) {
      rightIndex++;
    }

    const currentPeakLength = rightIndex - leftIndex - 1;

    longestPeak = Math.max(longestPeak, currentPeakLength);

    i = rightIndex;
  }


  return longestPeak;
}


const array = [1,2,3,3,4,0,10,6,5,-1,-3,2,3];
// output = 6 // 0,10,6,5,-1,-3
console.log(longestPeakII(array));
