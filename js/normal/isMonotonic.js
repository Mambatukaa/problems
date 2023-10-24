// Naive
// Space Complexity: O(1)
// Time Complexity: O(n)
const isMonotonic = (arr) => {
  if(arr.length < 2) {
    return true;
  }

  let isIncreasing = false;

  let j = 0;

  while(j < arr.length + 1) {
    const first = arr[j];
    const second = arr[j + 1];

    if(first === second) {
      j++;

      continue;
    }

    if(first < second) {
      isIncreasing = true;
    } else {
      isIncreasing = false;
    }

    break;
  }


  for(let i = 0; i < arr.length - 1; i++) {

    if(isIncreasing && arr[i] > arr[i+1]) {
      return false;
    }

    if(!isIncreasing && arr[i] < arr[i+1]) {
      return false;
    }
  }

  return true;
}


// Two pointers
// Space Complexity: O(1)
// Time Complexity: O(n)

const isMonotonicII = (arr) => {
  let isIncreasing = null;
  let leftIndex = 0;
  let rightIndex = 1;

  while(rightIndex < arr.length) {
    const left = arr[leftIndex];
    const right = arr[rightIndex];

    if(isIncreasing !== null) {
      if(isIncreasing && left > right) {
        return false;
      }

      if(!isIncreasing && left < right) {
        return false;
      }
    } else {

      if(left !== right) {
        isIncreasing = left < right ? true : false;
      }
    }

    rightIndex++;
    leftIndex++;



  }

  return true;
}

// Optimal solution
// Space Complexity: O(1)
// Time Complexity: O(n)
const isMonotonicIII = (arr) => {
  let isNonDecreasing = true;
  let isNonIncreasing = true

  for(let i = 0; i < arr.length; i++) {
    if(arr[i] < arr[i + 1]) isNonDecreasing = false;
    if(arr[i] > arr[i + 1]) isNonIncreasing = false;
  }

  return isNonIncreasing || isNonDecreasing;
}

// Space Complexity: O(1)
// Time Complexity: O(n)
const isMonotonicIV = (arr) => {
  if(arr.length < 2) {
    return true;
  }

  let direction = arr[1] - arr[0];


  for(let i = 2; i < arr.length; i++) {
    if(direction === 0) {

      direction = arr[i] - arr[i - 1];
      continue;
    }

    if(breakDirection(direction, arr[i - 1], arr[i])) {
      return false;
    }
  }

  return true;
}

const breakDirection = (direction , prev, curr) => {
  const diff = curr - prev;

  // increasing
  if(direction > 0)
    return diff < 0;

  // decreasing
  return diff > 0;
}


console.log(isMonotonicIV([5,4,3,2,1, 10]));
