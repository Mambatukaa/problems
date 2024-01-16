/**
 * @param {number[]} nums
 * @return {number}
 */
// Time Complexity: O(n * logn);
// Space Complexity: O(n)
var maximumSum = function(nums) {
    const map = new Map();
    let answer = -1;

    for(const num of nums) {
        const digitsSum = getDigitsSum(num);

        if(!map.has(digitsSum)) {
            map.set(digitsSum, []);
        };

        map.get(digitsSum).push(num);
    };

    for(const values of map.values()) {
        const n = values.length;

        if(n < 2) {
            continue;
        };

        values.sort((a, b) => a - b);

        answer = Math.max(answer, values[n - 1] + values[n - 2]);
    }


    return answer;
};

const getDigitsSum = (num) => {
    let answer = 0;

    while(num > 0) {
        answer += num % 10;
        num = Math.floor(num / 10);
    }

    return answer;
};


// Space Complexity: O(n)
// Time Complexity: O(n)
const maximumSumII = (nums) => {
  const map = new Map();
  let answer = -1;

  for(let i = 0; i < nums.length; i++) {
    let num = nums[i];
    let digitsSum = 0;

    // find digitsSum
    while(num > 0) {
      digitsSum += num % 10;
      num = Math.floor(num / 10);
    };

    // update answer
    if(map.has(digitsSum)) {
      answer = Math.max(answer, nums[i] + map.get(digitsSum));
    };

    const max = Math.max(nums[i], map.get(digitsSum) || 0);

    map.set(digitsSum, max);
  };

  return answer;
};

const nums = [279,169,463,252,94,455,423,315,288,64,494,337,409,283,283,477,248,8,89,166,188,186,128];

console.log(maximumSumII(nums));
