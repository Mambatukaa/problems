/**
 * @param {number[]} weight
 * @return {number}
 */
// Time Complexity: O(n log n)
// Space Complexity: O(n)
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
