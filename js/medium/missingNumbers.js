// Time Complexity: O(n)
// Space Complexity: O(n)
const missingNumbers = (nums) => {
  const output = [];
  const array = new Array(nums.length + 2).fill(1);


  for(const num of nums) {
    array[num-1] = -1;
  }

  for(let i = 0; i < array.length; i++) {
    if(array[i] === 1) {
      output.push(i+1);
    }

  }

  return output;
}

const nums = [1,4,3];

missingNumbers(nums);
