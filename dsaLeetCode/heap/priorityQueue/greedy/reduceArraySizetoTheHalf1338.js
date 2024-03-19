import { MaxPriorityQueue } from '@datastructures-js/priority-queue';

/**
 * @param {number[]} arr
 * @return {number}
 */

// Time Complexity: O(k * log k)
// Space Complexity: O(n)
var minSetSize = function(arr) {
  const map = new Map();
  const maxHeap = new MaxPriorityQueue();
  const n = arr.length;

  for(const num of arr) { 
    map.set(num, (map.get(num) || 0) + 1);
  };

  for(const value of map.values()) {
    maxHeap.enqueue(value);
  };

  let counter = 0;
  let currentTotal = n;

  while(currentTotal > n / 2) {
    currentTotal -= maxHeap.dequeue();
    counter++;
  };

  return counter;
};

// Time Complexity: O(n log n);
// Space Complexity: O(n);
var minSetSizeII = function(arr) {
  const map = new Map();
  const n = arr.length;
  let currentTotal = n;

  for(const num of arr) {
    map.set(num, (map.get(num) || 0) + 1);
  };

  const ordered = [];

  for(const value of map.values()) {
    ordered.push(value);
  }

  ordered.sort((a, b) => a - b);
  let counter = 0;

  /*
  map = {
    3: 4,
    5: 3,
    2: 2,
    7: 1
  };
  ordered = [4, 3, 2, 1]
  */

  while(currentTotal > n / 2) {
    // start to remove element from ordered list and update current total
    currentTotal -= ordered.pop();
    counter++;
  };

  return counter;
};

const arr = [3,3,3,3,5,5,2,2,7];

console.log(minSetSize(arr));
console.log("========================");
console.log(minSetSizeII(arr));

/*

Input: arr = [3,3,3,3,5,5,5,2,2,7];
  n = 10;

Output: 2

Explanation: Choosing {3,7) will make the new array [5,5,5,2,2] which has size 5 (i.e equal to half of the size of the old array).

Possible sets of size 2 are {3,5},{3,2},{5,2}.

Choosing set (2,7) is not possible as it will make the new array [3,3,3,3,5,5,5] which has a size greater than half of the size of the old
array.


return min size of the set that

n = 10;
remove at least half of the integers from an array
if we remove 3 and 7 from the array. [5, 5, 5, 2, 2] total set is = 2;

declare counter;

1. Start to remove set which has most element.
  a. and increase the counter
  b. and compare the current size with n / 2;

if(current array size reaches the limit) {
  return counter
} else {
  repeat.
}


[3, 3, 3, 3, 5, 5, 5, 2, 2, 7]

this example we have

{
  3: 4,
  5: 3,
  2: 2,
  7: 1
} we have 4 sets with values

1. Remove 3 which has the most elements
  counter = 1;
  arr = [5,5,5,2,2,7] size = 6 which is greater than half of 10 that is original array size

  repeat
  updated list {
    5: 3,
    2: 2,
    7: 1
  }

  now we will delete 5 and check the array size


  1. To remove the set which has most element we have to count collections using map
  2. Then sort the map by total values
  3. and then remove the max value and compare the current values sum to n / 2
  4. return counter;




*/
