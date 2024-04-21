import {
  MinPriorityQueue,
} from '@datastructures-js/priority-queue';

// Time Complexity: O(m * n);
// Space Complexity: O(n);

const getMinimumCost = (n, a, b, m) => {
  const calculate = (i, j) => {
    return a[i] + (j - 1) * b[i];
  };

  const minHeap = new MinPriorityQueue();
  let j = 1;
  let total = 0;

  // add calculated item to heap 
  // when calculated item reaches the limit get the min item and increase the total
  // when heap become empty increase the j and calculate the items again
  // Retreat the above step until m reaches the 0 which is we purchased all data in min price;
  
  while(m > 0) {

    // calculate all values in current j
    for(let i = 0; i < n; i++) {
      const price = calculate(i, j);

      minHeap.enqueue(price);
    };

    while(minHeap.size()) {
      const min = minHeap.dequeue();
      console.log(min, m, j )
      total += min

      m--;

      if(m === 0) {
        break;
      }
    };

    j++;
  }

  return total;
};

const n = 3;
const a = [1, 3, 2];
const b = [2, 1, 3];
const m = 5;


console.log('res: ', getMinimumCost(n, a, b, m))

