import { MaxPriorityQueue } from "@datastructures-js/priority-queue";

// Time Complexity: O(n * log k)
// Space Complexity: O(n)
var kClosest = function(points, k) {
  const maxHeap = new MaxPriorityQueue(item => item.distance);

  // calculate the distance and add to the max heap
  // if queue size reach the limit remove elements from heap
  // if it's max heap the only max value will be deleted
  // after calculation the only k elements will left in the heap

  for(const [index, [x, y]] of points.entries()) {
    const distance = Math.pow(x, 2) + Math.pow(y, 2);

    maxHeap.enqueue({
      index,
      distance
    });

    if(maxHeap.size() > k) {
      maxHeap.dequeue();
    };

  };

  const answer = [];

  while(maxHeap.size()) {
    const index = maxHeap.dequeue().index;

    answer.push(points[index]);
  };
    
  return answer;
};

const points = [[3,3],[5,-1],[-2,4]], k = 2

console.log(kClosest(points, k));


/**
 * @param {number[][]} points
 * @param {number} k
 * @return {number[][]}
 */
 // Time Complexity: O(n * log n)
 // Space Complexity: O(n)
var kClosestII = function(points, k) {
  const arr = [];

  for(let i = 0; i < points.length; i++) {
    const [x, y] = points[i];

    arr.push([i, Math.pow(x, 2) + Math.pow(y, 2)]);
  };

  arr.sort((a, b) => a[1] - b[1]);

  const answer = [];

  while(k > 0) {
    const [idx] = arr.shift();

    answer.push(points[idx])

    k--;
  };

    
  return answer;
};

 // Time Complexity: O(n * log n)
 // Space Complexity: O(n)
var kClosestIII = function(points, k) {
  const distance = ([x, y]) => x * x + y * y;

  points.sort((a, b) => distance(a) - distance(b));

  return points.slice(0, k);
};

/*
  Input: points = [[1,3],[-2,2]], k = 1

  Output: [[-2,2]]

  Explanation:
  The distance between (1, 3) and the origin is sqrt(10).
  The distance between (-2, 2) and the origin is sqrt(8).
  Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
  We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].


  // NAIVE APPROACH

  1. find the distance on each item.
  2. and add index and item distance to the array
  3. sort the array by distance
  4. add the closest values to the answer array
  5. return answer.

*/
