/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
 // 15 minutes
var topKFrequent = function(nums, k) {
  const maxHeap = new MaxPriorityQueue((item) => item.value);
  const map = new Map();

  for(const num of nums) {
    map.set(num, (map.get(num) || 0) + 1);
  };

  for(const [key, value] of map) {
    maxHeap.enqueue({
      key,
      value
    })
  };

  const answer = []; 

  for(let i = 0; i < k; i++) {
    answer.push(maxHeap.dequeue().key);
  };

  return answer;
};


/*
top K frequent

Time Complexity must be better than O(n log n); // No sort
k is in the range [1, the number of unique elements in the array]; (k is valid)
ANSWER IS UNIQUE (Guaranteed)

Input: nums = [1, 1, 1, 2, 2, 3], k = 2;
Output: [1, 2];

Map = {
  1: 3,
  2: 2,
  3: 1
};

Sort the keys based on values O(n log n)

1. Count elements using map and return max k keys which counts higher than others. Time Complexity: O( n log n) Space Complexity: O(n)



2. OPTIMAL SOLUTION

MAX HEAP 
Time Complexity: O(n)
Space Complexity: O(n)
*/


