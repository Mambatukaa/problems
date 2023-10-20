// Time complexity: O(log(n))
// Space complexity: O(1)
const binarySearch = (arr, target) => {
  let left = 0;
  let right = arr.length - 1;

  while(left <= right) {
    const midIndex = Math.floor((left + right) / 2 );

    console.log("midIndex:", midIndex);

    if(arr[midIndex] === target) {
      return midIndex;
    }

    if(arr[midIndex] > target) {
      right = midIndex - 1;
    } else {
      left = midIndex + 1;
    }
  }

  return -1;
}

// Time complexity: O(log(n))
// Space complexity: O(n)
const binarySearchII = (arr, target, left = 0, right = arr.length) => {
  if(left > right) {
    return -1;
  }

  const midIndex = Math.floor((left + right) / 2)
  const potentialMatch = arr[midIndex];

  if(potentialMatch === target) {
    return midIndex;
  }

  if(potentialMatch > target) {
    return binarySearchII(arr, target, left, midIndex - 1);
  } else {
    return binarySearchII(arr, target, midIndex + 1, right);
  }
  
}


console.log(binarySearchII([1,2,3,4,5,6], 6));
// 3
