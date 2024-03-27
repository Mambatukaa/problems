 /*
 * @param {number[]} sweetness
 * @param {number} k
 * @return {number}
 */

 // Time Complexity: O(n * log(S/(k + 1)))
 // Space Complexity: O(1)
var maximizeSweetness = function(sweetness, k) {
  let left = 1;
  let right = Math.floor(sweetness.reduce((a, b) => a + b) / (k + 1));

  while(left <= right) {
    const value = Math.floor((left + right) / 2);

    let totalChunks = 0;
    let sumOfChunks = 0;

    for(const sweet of sweetness) {
      sumOfChunks += sweet;

      // if total of chunks reaches the limit split the chunk
      if(sumOfChunks >= value) {
        totalChunks++;
        sumOfChunks = 0;
      };

      if(totalChunks >= k + 1) {
        break;
      };
    };

    if(totalChunks <= k) {
      right = value - 1;
    } else {
      left = value + 1;
    };
  };

  return right;
};

// Naive approach
// Time Complexity: O(m * n) m = S / k + 1
// Space Complexity: O(1)
var maximizeSweetnessII = function(sweetness, k) {
  let value = 1;

  /*
    sweetness = [1,2,2,1,2,2,1,2,2]
    k = 2;
  */

  while(true) {
    let totalChunks = 0;
    let sumOfChunks = 0;

    for(const sweet of sweetness) {
      sumOfChunks += sweet;

      // if total of chunks reaches the limit split the chunk
      if(sumOfChunks >= value) {
        totalChunks++;
        sumOfChunks = 0;
      };

      console.log(value, totalChunks, sumOfChunks)

      if(totalChunks >= k + 1) {
        value++;
        break;
      };
    };

    if(totalChunks <= k) {
      return value - 1;
    };
  };
};
