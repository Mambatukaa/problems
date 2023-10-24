// Time Complexity: O(n)
// Space Complexity: O(1)
const moveElementToEnd = (array, toMove) => {
  let leftIndex = 0;
  let rightIndex = array.length - 1;

  while(leftIndex < rightIndex) {

    if(array[leftIndex] !== toMove) {
      leftIndex++;
      continue;
    }

    if(array[rightIndex] === toMove) {
      rightIndex--;
      continue;
    }

    // swap

    [array[leftIndex], array[rightIndex]] = [array[rightIndex], array[leftIndex]];

    rightIndex--;
    leftIndex++;
  }

  return array;
}

const moveElementToEndII = (array, toMove) => {
  let leftIndex = 0;
  let rightIndex = array.length - 1;

  while(leftIndex < rightIndex) {

    while(leftIndex < rightIndex && array[rightIndex] === toMove) rightIndex--;
    if(array[leftIndex] === toMove) [array[leftIndex], array[rightIndex]] = [array[rightIndex], array[leftIndex]];
    leftIndex++;
  }

  return array;
}


console.log(moveElementToEndII([2,1,2,2,2,3,4,2], 2));
