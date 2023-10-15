// Time Complexity: O(n^2)
// Space Complexity: O(1)
const selectionSort = (array) => {

  for(let i = 0; i < array.length; i++) {
    let minIndex = i;

    for(let j = i + 1; j < array.length; j++) {
      if(array[minIndex] > array[j]) {
        minIndex = j;
      }
    }

    [array[i], array[minIndex]] = [array[minIndex], array[i]];
  }

  return array;
}

console.log(selectionSort([5,4,3,2,1]));
