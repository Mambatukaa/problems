/**
 * @param {number[]} nums
 * @return {number[][]}
 */
 // Three pointers (SORT & TWO POINTERS)
 // Time Complexity: O(n^2)
 // Space Complexity: O(n)
 // 20 minutes
var threeSum = function(nums) {
  const res = [];
  if(nums.length < 3) {
    return res;
  };

  // remove duplicates
  nums.sort((a, b) => a - b);

  const target = 0;

  const duplication = new Set();

  for(let i = 0; i < nums.length; i++) {
    const curr = nums[i];
    const diff = target - curr;

    let leftIdx = i + 1;
    let rightIdx = nums.length - 1;

    while(leftIdx < rightIdx) {
      const sum = nums[leftIdx] + nums[rightIdx];

      if(sum === diff) {
        const pair = `${curr},${nums[leftIdx]},${nums[rightIdx]}`;

        if(!duplication.has(pair)) {
          duplication.add(pair);
          res.push([curr, nums[leftIdx], nums[rightIdx]])
        };
      };

      if(sum > diff) {
        rightIdx--;
      } else {
        leftIdx++;
      }
    };
  };

  return res;
    
};


/*

1. Target = 0;
    nums[i] + nums[j] + nums[k] = 0;

    i, j, k must be different indexes.


nums = [-1, 0, 1, 2, -1, -4]

Output: [[-1, -1, 2], [-1, 0, 1]];


1. Brute force Time Complexity: O(n^3)


2. Look for solution which is less than O(n^3)

SORTING and TWO POINTERS

nums = [-4, -1, -1, 0, 1, 2]

1. Start from the first element and find difference between target and first element. Search difference from other elements. 
    The array is sorted then use two pointers on other elements.


-4
  diff = -4 - 0 = -4;

  search -4 pair from other elements using 2 pointers

   L    R
  [-1, -1, 0, 1, 2]

  L + R = -1 + 2 => 1; 
    L = 0; R = 4;
    1 > - 4
    move right pointer
    R--;

  L + R = -1 + 1 => 0;
    L = 0; R = 3;
    0 > -4
    move right pointer
    R--;

  L + R = -1 + 0 => -1;
    L = 0; R = 2;
    -1 > -4
    move right pointer
    R--;

  L + R = -1 + -1 => -2;
    L = 0; R = 1;
    -2 > -4
    move right pointer
    R--;

  Reach the limit no pair founded.

  try the above step with next value.

  if pair founded 
    add to the answer array

  Time Complexity: O(n^2 + n log n) ===> O(n^2)
  Space Complexity: O(n)



*/
