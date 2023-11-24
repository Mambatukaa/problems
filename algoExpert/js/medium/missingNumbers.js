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

// Time Complexity: O(n)
// Space Complexity: O(n)
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

// Time Complexity: O(n)
// Space Complexity: O(1)
const missingNumbersIII = (nums) => {
  let total = sum(1, nums.length + 3);

  for(const num of nums) {
    total -= num;
  }

  const averageMissingValue = Math.floor(total / 2);

  let foundFirstHalf = 0;
  let foundSecondHalf = 0;

  for(const num of nums) {
    if(num <= averageMissingValue) {
      foundFirstHalf += num;
    } else {
      foundSecondHalf += num;
    }
  }

  const expectedFirstHalf = sum(1, averageMissingValue + 1);
  const expectedSecondHalf = sum(averageMissingValue + 1, nums.length + 3);

  console.log(expectedFirstHalf, '=====', expectedSecondHalf)

  return [expectedFirstHalf - foundFirstHalf, expectedSecondHalf - foundSecondHalf]
  
}

const sum = (a, b) => {
  let total = 0;

  for(let num = a; num < b; num++) {
    total += num;
  }

  return total;
}

// Time Complexity: O(n)
// Space Complexity: O(1)
const missingNumbersIV = () => {
  let solutionXOR = 0;
  for (let i = 0; i < nums.length + 3; i++) {
    solutionXOR ^= i;
    if (i < nums.length) {
      solutionXOR ^= nums[i];
    }
  }

  const solution = [0, 0];
  const setBit = solutionXOR & -solutionXOR;
  for (let i = 0; i < nums.length + 3; i++) {
    if ((i & setBit) === 0) {
      solution[0] ^= i;
    } else {
      solution[1] ^= i;
    }

    if (i < nums.length) {
      if ((nums[i] & setBit) === 0) {
        solution[0] ^= nums[i];
      } else {
        solution[1] ^= nums[i];
      }
    }
  }

  solution.sort((a,b) => a-b);

  return solution;
}

const nums = [1,3,4];

console.log(missingNumbersIV(nums));
