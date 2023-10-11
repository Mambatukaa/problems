// Time complexity: O(n)
// Space complexity: O(1)
const findThreeLargets = (arr) => {
  let first = Number.MIN_SAFE_INTEGER;
  let second = Number.MIN_SAFE_INTEGER;
  let third = Number.MIN_SAFE_INTEGER;

  for(let num of arr) {
    if(num > first) {
      third = second;
      second = first;
      first = num;
    } else if(num > second) {
      third = second;
      second = num;
    } else if(num > third) {
      third = num;
    }

  }

  return [third, second, first];
}


console.log(findThreeLargets([-100,-10, -1]));
