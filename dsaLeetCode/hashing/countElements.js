// Space Complexity: O(n)
// Time Complexity: O(n)
const countElements = (arr) => {
  const seen = new Set(arr);

  let counter = 0;

  for(const num of arr) {
    if(seen.has(num + 1)) {
      counter++;
    }
  }

  return counter;
};

// Time Complexity: O(n logn)
// Space Complexity: O(1)
const countElementsII = (arr) => {
  arr.sort((a, b) => a - b);

  let runLength = 1;
  let counter = 0;

  for(let i = 1; i < arr.length; i++) {

    if(arr[i-1] !== arr[i]) {
      if(arr[i-1] + 1 === arr[i]) {
        counter += runLength;
      };

      runLength = 0;
    };

    runLength++;
  };


  return counter;
};


const arr = [1,1,1,2,2,4,5,6,8,8,9,12,12,12,12,13,13];

console.log(countElementsII(arr));

