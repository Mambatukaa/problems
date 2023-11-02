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

const missingNumbersII = (nums) => {
  const output = [];
  const set = new Set(nums);

  for(let num = 1; num < nums.length + 3; num++) {
    if(!set.has(num)) {
      output.push(num);
    }
  }

  return output;
}

const nums = [1,4,3];

missingNumbers(nums);
