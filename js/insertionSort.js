// Time Complexity: O(n^2)
// Space Complexity: O(1)
const insertionSort = (array) => {
  for(let i = 1; i < array.length; i++) {
    const num = array[i];

    for(let j = i; j > 0; j--) {
      const prevNum = array[j - 1];

      if(num < prevNum) {
        // switch
        array[j] = prevNum;
        array[j-1] = num;
      }
    }

  }

  return array;
}

// Time Complexity: O(n^2)
// Space Complexity: O(1)
const insertionSortII = (array) => {

  for(let i = 1; i < array.length; i++) {

    for(let j = i; j > 0; j--) {
      console.log(array[j], array[j-1]);

      if(array[j] < array[j-1]) {
        // switch
        [array[j], array[j-1]] = [array[j-1], array[j]];
      }

    }

  }

  return array;
}


console.log(insertionSortII([3,2,1]));
