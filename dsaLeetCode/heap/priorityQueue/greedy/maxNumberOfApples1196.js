/**
 * @param {number[]} weight
 * @return {number}
 */
// Sort also we can use min Heap and Counting sort
// Time Complexity: O(n log n)
// Space Complexity: O(1)
var maxNumberOfApples = function(weight) {
  weight.sort((a, b) => a - b);

  let counter = 0;
  let limit = 0;

  for(const apple of weight) {
    limit += apple;

    if(limit > 5000) {
      return counter;
    };

    counter++;

  };

  return counter;

};
