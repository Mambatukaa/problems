// Space Complexity: O(n)
// Time Complexity: O(n)
const arrayOfProducts = (array) => {

  const answer = [];

  for(let i = 0; i < array.length; i++) {
    let total = 1;

    for(let j = 0; j < array.length; j++) {
      if(i === j) {
        continue;
      }

      if(array[j] === 0){
        answer[i] = 0;
        break;
      }

      total *= array[j];

      answer[i] = total;
    }
  }

  return answer;
}

// Space Complexity: O(1)
// Time Complexity: O(n)
// Used division
const arrayOfProductsII = (array) => {
  let zeroCounter = 0;
  let total = 1;

  for(const num of array) {
    if(num === 0) {
      zeroCounter++;

      continue;
    }

    total *= num;
  }


  if(zeroCounter > 1) {
    return array.fill(0);
  }

  for(let i = 0; i < array.length; i++) {
    if(zeroCounter === 1 && array[i] === 0) {
      array.fill(0);
      array[i] = total;
      break;
    }

    array[i] = total / array[i];
  }

  return array;
}

// Time Complexity: O(n)
// Space Complexity: O(n)
const arrayOfProductsIII = (array) => {
  const products = new Array(array.length).fill(1);

  const leftProducts = new Array(array.length).fill(1);
  const rightProducts = new Array(array.length).fill(1);


  let leftRunningProduct = 1;

  for(let i = 0; i < array.length; i++) {
    leftProducts[i] = leftRunningProduct;
    leftRunningProduct *= array[i];
  }

  let rightRunningProduct = 1;

  for(let i = array.length - 1; i >= 0 ; i--) {
    rightProducts[i] = rightRunningProduct;
    rightRunningProduct *= array[i];
  }

  for(let i = 0; i < array.length; i++) {
    products[i] = leftProducts[i] * rightProducts[i];
  }

  return products;
}

// Time Complexity: O(n)
// Space Complexity: O(n)
const arrayOfProductsIV = (array) => {
  const result = new Array(array.length).fill(1);

  let leftRunningProduct = 1;

  for(let i = 0; i < array.length; i++) {
    result[i] = leftRunningProduct;

    leftRunningProduct *= array[i];
  }

  let rightRunningProduct = 1;

  for(let i = array.length - 1; i >= 0 ; i--) {
    result[i] = result[i] * rightRunningProduct;
    rightRunningProduct *= array[i];
  }

  return result;
}

const array = [1,2,3,4];

console.log(arrayOfProductsIV(array));
