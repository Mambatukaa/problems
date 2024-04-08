/**
 * @param {number[]} nums
 * @return {boolean}
 */

// 2 minutes
var containsDuplicate = function(nums) {

  const seen = new Set();

  for(const num of nums) {
    if(seen.has(num)) {
      return true;
    };

    seen.add(num);
  }
    
  return false;
};

/*
1. Brute force
  Time Complexity: O(n^2)
  Space Complexity: O(1)

2. HashTable (SET)
  Time Complexity: O(n)
  Space Complexity: O(n)

3. Sort and compare
  Time Complexity: O(n log n)
  Space Complexity: O(1)


*/
