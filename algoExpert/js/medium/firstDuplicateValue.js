// Time Complexity: O(n^2)
// Space Complexity: O(1)
const firstDuplicateValue = (array) => {
  let minSecondIndex = array.length;

  for(let i = 0; i < array.length; i++) {

    for(let j = i + 1; j < array.length; j++) {
      if(array[i] === array[j]) {
        minSecondIndex = Math.min(minSecondIndex, j);
      }
    }
  }

  if(minSecondIndex === array.length) return -1;

  return array[minSecondIndex];
}

// Time Complexity: O(n)
// Space Complexity: O(n)
const firstDuplicateValueII = (array) => { 
  const set = new Set();

  for(const num of array) {
    if(set.has(num)) {
      return num;
    }

    set.add(num);
  }

  return -1;
}

// work only between 1 and n
// Time Complexity: O(n)
// Space Complexity: O(1)
const firstDuplicateValueIII = (array) => { 

  for(const num of array) {
    const absValue = Math.abs(num);

    if(array[absValue - 1] < 0) return absValue;

    array[absValue - 1] *= -1;

    console.log(array)
  }

  return -1;
}

console.log(firstDuplicateValueIII([1,20,100,100]));
