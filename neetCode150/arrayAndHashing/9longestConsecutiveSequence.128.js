import { MinPriorityQueue } from '@datastructures-js/priority-queue';
/**
 * @param {number[]} nums
 * @return {number}
 */
// 10 minutes
// Time Complexity: O(n)
// Space Complexity: O(n)
var longestConsecutive = function(nums) {
  if(!nums.length) return 0;

  const minHeap = new MinPriorityQueue();
  const seen = new Set();

  for(const num of nums) {
    if(seen.has(num)) {
      continue;
    };

    seen.add(num);

    minHeap.enqueue(num);
  };

  console.log(minHeap.toArray())

  let max = 1;
  let counter = 1;
  let prev = minHeap.dequeue();

  while(minHeap.size()) {
    const curr = minHeap.dequeue();

    if(prev + 1 === curr) {
      counter++;
    } else {
      counter = 1;
    };

    max = Math.max(counter, max);

    prev = curr;
  };

  return max;
};

// Time Complexity: O(n * k)
// Space Complexity: O(n)
var longestConsecutiveII = function(nums) {
  const seen = new Set(nums);
  let longest = 0;

  for(const num of nums) {
    if(!seen.has(num - 1)) {
      let counter = 1;

      while(seen.has(num + counter)){
        counter++;
      };

      longest = Math.max(longest, counter);
    }
  };

  return longest;
};

console.log(longestConsecutiveII([0,3,7,2,5,8,4,6,0,1]))


// min heap
// add nums to the heap

// and iterate through heap and count consecutive
// if 

