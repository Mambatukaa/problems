// Space Complexity: O(1)
// Time Complexity: O(n * logn)
const nonConstructibleChange = (coins) => {
  coins.sort((a,b) => a-b);

  let change = 0;

  for(let coin of coins) {
    if(change + 1 < coin) {
      return change + 1;
    }

    change += coin;
  }

  return change + 1;
}


console.log(nonConstructibleChange([2,3]));
