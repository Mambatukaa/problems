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


const array = [0,0,0,0];

console.log(arrayOfProducts(array));
