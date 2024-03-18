import {
  PriorityQueue,
} from '@datastructures-js/priority-queue';

// Time Complexity: O(n * log k)
// Space Complexity: O(n)
//const arr = [1,2,3,4,5];
var findClosestElements = function(arr, k, x) {
  const heap = new PriorityQueue((a, b) => {

    console.log(a, 'ahhaha', b, "diff:", Math.abs(a - x), Math.abs(b - x))

    // same diff
    if(Math.abs(a - x) === Math.abs(b - x)) {
      return b - a;
    };
    
    return Math.abs(b - x) - Math.abs(a - x);
  });

  for(const num of arr) {
    heap.enqueue(num);

    if(heap.size() > k) {
      heap.dequeue();
    }
  };

  console.log(heap.toArray(), '----------------')


  return heap.toArray().sort((a, b) => a - b);
};

 // Time Complexity: O(n * log n) // sort
 // Space Complexity: O(n)
var findClosestElementsII = function(arr, k, x) {
  const nums = [];

  for(let i = 0; i < arr.length; i++) {
    const curr = arr[i];
    const diff = Math.abs(x - curr);

    nums.push([i, diff]);
  };

  nums.sort((a, b) => a[1] - b[1]);

  const answer = [];

  while(k > 0) {
    const [idx] = nums.shift();
    answer.push(arr[idx])

    k--;
  };


return answer.sort((a, b) => a - b)
};



const arr = [1,2,3,4,5];
const k = 4;
const x = 3;

console.log(findClosestElements(arr, k, x))
