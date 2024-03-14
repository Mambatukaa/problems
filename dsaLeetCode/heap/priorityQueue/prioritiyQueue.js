import {
  MaxPriorityQueue,
} from '@datastructures-js/priority-queue';


// Time Complexity: O(n log k)
// Space Complexity: O(n)
var topKFrequent = function(nums, k) {
  const maxHeap = new MaxPriorityQueue(item => item.value);
  const map = new Map();

  for(const num of nums) {
    map.set(num, (map.get(num) || 0) + 1);
  };

  for(const [key, value] of map) {
    maxHeap.enqueue({
      key,
      value
    });
  };

  const answer = [];

  for(let i = 0; i < k; i++) {
    const max = maxHeap.dequeue();

    answer.push(max.key);
  };

  return answer;
};

 // Time Complexity: O(n log n);
 // Space Complexity: O(n)
var topKFrequentII = function(nums, k) {
  let map = new Map();

  for(const num of nums) {
    map.set(num, (map.get(num) || 0) + 1);
  };

  map = new Map([...map.entries()].sort((a, b) => b[1] - a[1]));

  const keys = Array.from(map.keys());
  const answer = [];
  for(let i = 0; i < k; i++) {
    answer.push(keys[i]);
  };

  return answer;

  /*
    map = {
      1: 3,
      2: 2,
      3: 1
    };
  */

  // sort by descending order using values
    
};

/*

naive approach

1. use Map and store nums with count
2. sort the map
3. return the first k keys that count is higher



*/

const nums = [1,1,1,2,2,3], k = 2;

console.log(topKFrequent(nums, k));
