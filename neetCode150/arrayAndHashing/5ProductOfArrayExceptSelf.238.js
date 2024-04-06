/**
 * @param {number[]} nums
 * @return {number[]}
 */

var productExceptSelf = function(nums) {
  const n = nums.length;
  const res = new Array(n).fill(0);
  let prefix = 1;
  let postfix = 1;

  for(let i = 0; i < n; i++) {
    res[i] = prefix;
    prefix *= nums[i];
  };

  for(let i = n - 1; i >= 0; i--) {
    res[i] *= postfix;
    postfix *= nums[i];
  };

  console.log(res)

  return res;

/*
  res[0] = 1;
  prefix *= 1;

  res[1] = 1;
  prefix *= 2;

  res[2] = 2;
  prefix *= 6;

  res[3] = 6;
  prefix *= 4; (24)

  res = [1, 1, 2, 6]

  res[3] *= 1;
  postfix *= 4

  res[2] *= 4;
  postfix *= 3;


  res[1] *= 12;
  postfix *= 2;

  res[0] *= 24;
  postfix *= 1;


   nums = [1, 2, 3, 4];
 prefix = [1, 2, 6, 24]
postfix = [24, 24, 12, 4]

 answer = [24, 12, 4, 6]

before prefix, after postfix

i = 0; prefix[i - 1] * postfix[i + 1] === prefix[-1] * postfix[1];

*/


};
  // Time Complexity: O(3n) === O(n)
  // Space Complexity: O(1)
var productExceptSelfII = function(nums) {
  const arr = new Array(nums.length).fill(0);
  let totalMultipication = 1;
  let zeroesCount = 0;

  for(const num of nums) {
    if(num === 0) {
      zeroesCount++;

      if(zeroesCount === 2) {
        return arr;
      };

      continue;
    };

    // calculate multiplication with no zeroes
    totalMultipication *= num;
  };

  if(zeroesCount === 1) {
    const idx = nums.indexOf(0);

    arr[idx] = totalMultipication;
    return arr;

  } 

  for(let i = 0; i < nums.length; i++) {
    nums[i] = totalMultipication / nums[i];
  };
    
  return nums;
};


/*

Input: nums = [1,2,3,4]; Product of all elements = 1 * 2 * 3 * 4 = 24; 
  [24 / 1 = 24, 24 / 2 = 12, 24 / 8 = 3, 24 / 4 = 6]
Output: [24, 12, 8, 6];


Example 2:

Input: nums = [-1, 1, 0, -3, 3];

-1 * 1 * 0 * -3 * 3 ===== 0;

         x
-1 * 1 * 0 * -3 * 3 ===== 0;

-1 * 1 * -3 * 3 = 9;

Output: [0, 0, 9, 0, 0];

1. SOLVE THE PROBLEM WITH O(1) TIME COMPLEXITY; no additional space and data structure;
2. TIME COMPLEXITY: O(n) NO DIVISION OPERATION


nums = [-1, 1, 0, -3 , 3];

1. Brute force
  Time Complexity: O(n^2)
  Space Complexity: O(1)

2. Iterate through nums
    zeroesCount = 0;
    zeroesIndex = 0;

  
  total multipication (without zero)


if(zeroesCount > 1) {
  return nums.fill(0);
};

if(zeroesCount === 0) {
  for(let i = 0; i < nums.length; i++) {
    nums[i] = totalMultipication / nums[i]
  }
} else {
  replace nums[zeroIdx] = totalMultipication;
};


return answer;




*/
