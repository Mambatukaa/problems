/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {

  const map = new Map();

  for(let i = 0; i < nums.length; i++) {
    const num = nums[i];
    const diff = target - num;

    if(map.has(diff)) {
      return [map.get(diff), i];
    };

    map.set(num, i);
  };

  return [];
};


/*

1. Brute force
  Time Complexity: O(n^2)
  Space Complexity: O(1)

2. Sort and Two Pointers
  Time Complexity: O(n log n)
  Space Complexity: O(1)

3. Hash Table (HashMap)

  Store the elements and search the difference of current element and target from the Map. If it's found return indexes;

  Time Complexity: O(n)
  Space Complexity: O(n)
*/
