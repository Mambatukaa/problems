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


const array = [1,2,3,3,4,0,10,6,5,-1,-3,2,3];
// output = 6 // 0,10,6,5,-1,-3
console.log(longestPeak(array));
