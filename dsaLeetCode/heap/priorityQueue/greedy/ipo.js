/**
 * @param {number} k
 * @param {number} w
 * @param {number[]} profits
 * @param {number[]} capital
 * @return {number}
 */
 // Time Complexity: O(n * logn)
 // Space Complexity: O(n)
var findMaximizedCapital = function(k, w, profits, capital) {

  const n = profits.length;
  const maxHeap = new MaxPriorityQueue();

  // sort capital and profit based on capital
  const capitalProfit = [];

  for(let i = 0; i < n; i++) {
    capitalProfit.push([capital[i], profits[i]]);
  };

  capitalProfit.sort((a, b) => a[0] - b[0]);

  let totalCapital = w;

  let i = 0;

  while(k > 0) {
    // can we afford
    while(i < n && totalCapital >= capitalProfit[i][0]) {
      maxHeap.enqueue(capitalProfit[i][1]);
      i++;
    };

    if(!maxHeap.size()) {
      return totalCapital;
    };

    totalCapital += maxHeap.dequeue().element;

    k--;
  }


  return totalCapital;


  

} 

// TIME LIMIT EXCEEDED
// Time Complexity: O(n log n * n)
// Space Complexity: O(n)
var findMaximizedCapitalII = function(k, w, profits, capital) {
  let totalCapital = w;
  const n = capital.length;
  const seenIdx = new Set();

  const capitalProfits = [];

  for(let i = 0; i < n; i++) {
    capitalProfits.push([capital[i], profits[i]])
  };

  capitalProfits.sort((a, b) => a[1] - b[1]);

  while(k > 0) {

    for(let i = n - 1; i >= 0; i--) {
      // skip the already calculated profit
      if(seenIdx.has(i)) {
        continue;
      };

      // find capital we can implement
      if(capitalProfits[i][0] <= totalCapital) {
        seenIdx.add(i);
        
        // increase total capital
        totalCapital += capitalProfits[i][1];
        break;
      };

    };

    k--;
  };

  return totalCapital;
};

