/**
 * @param {number[]} piles
 * @param {number} k
 * @return {number}
 */

// Naive approach
// Time Complexity: O(k * n log n)
// Space Complexity: O(1)
var minStoneSum = function(piles, k) {
  // sort and reduce max element
  const n = piles.length;

  for(let i = 0; i < k; i++) {
    piles.sort((a, b) => a - b);
    const max = piles[n - 1];

    piles[n-1] = max - Math.floor(max / 2);
  };

  let total = 0;

  for(const pile of piles) {
    total += pile;
  };

  return total;
};

// Time Complexity: O(n)
// Space Complexity: O(1)
var minStoneSum = function(piles, k) {
    const maxHeap = new MaxPriorityQueue();
    
    // build max heap using piles
    for(const pile of piles) {
        maxHeap.enqueue(pile);
    };
    
    // reduce the max element k times
    for(let i = 0; i < k; i++) {
      const max = maxHeap.dequeue().element;
      const removingValue = Math.floor(max / 2)

      const num = max - removingValue;
      
      // add half of max to the heap
      maxHeap.enqueue(num);
    };

    let total = 0;

    while(maxHeap.size()) {
      total += maxHeap.dequeue().element;
    };
    
    
    return total;
    
};

