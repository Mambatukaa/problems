import {
  MinPriorityQueue,
} from '@datastructures-js/priority-queue';

/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
 // Time Complexity: O(n * log k)
 // Space Complexity: O(n)
var findKthLargest = function(nums, k) {
    const minHeap = new MinPriorityQueue();
    
    for(const num of nums) {
        minHeap.enqueue(num);

        if (minHeap.size() > k) {
            minHeap.dequeue();
        }
    };
    
    
    return minHeap.front().element;
};
