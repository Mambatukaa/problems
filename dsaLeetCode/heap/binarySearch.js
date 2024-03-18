


const binarySearchAdd = (arr, num) => {
  if(!arr.length) {
    arr.push(num);
    return;
  };

  let low = 0;
  let high = arr.length - 1;

  while(low <= high) {
    const midIdx = Math.floor((low + high) / 2);

    if(arr[midIdx] <= num) {
      // go right
      low = midIdx + 1;
    } else {
      high = midIdx - 1;
    }
  };

  arr.splice(low, 0, num);
};

const arr = [];

binarySearchAdd(arr, 1);
binarySearchAdd(arr, 2);
binarySearchAdd(arr, 3);
binarySearchAdd(arr, -1);
binarySearchAdd(arr, 7);
binarySearchAdd(arr, 5);

console.log(arr)
