// Best TC: O(n) SC: O(1)
// Time Complexity: O(n^2)
// Space Complexity: O(1)
const bubbleSort = (arr) => {
  let isSwitch = true;

  while(isSwitch) {
    isSwitch = false;

    for(let i = 0; i < arr.length - 1; i++) {
      if(arr[i] > arr[i+1]) {
        isSwitch = true;

        const temp = arr[i];
        arr[i] = arr[i + 1];
        arr[i+1] = temp;
      }
    }
  }

  return arr;
}

// Best TC: O(n) SC: O(1)
// Time Complexity: O(n^2)
// Space Complexity: O(1)
const bubbleSortII = (arr) => {
  let isSorted = false;
  let counter = 0;

  while(!isSorted) {
    isSorted = true;

    for(let i = 0; i < arr.length - 1 - counter; i++) {
      if(arr[i] > arr[i + 1]) {
        isSorted = false;

        [arr[i], arr[i+1]] = [arr[i + 1], arr[i]];
      }

    }

    counter++;
  }

  return arr;
}


console.log(bubbleSortII([5,4,3,2,1]));
