// Time Complexity: O(n) 
// Space Complexity: O(d) 
// n is the total number of elements in the array
// d is greatest depth of "special" arrays
const productSum = (item, level = 1) => {
  let sum = 0;

  for(let el of item) {
    if(Array.isArray(el)) {
      sum += productSum(el, level + 1);
    } else {
      sum += el;
    }
  }

  console.log(sum);

  return level * sum;
}



console.log(productSum([0, 2, [3,4]]));
