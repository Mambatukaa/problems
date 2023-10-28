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


const array = [2,1,2,3];

console.log(arrayOfProductsII(array));
