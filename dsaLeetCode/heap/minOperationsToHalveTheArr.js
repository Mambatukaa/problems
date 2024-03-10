/**
 * @param {number[]} nums
 * @return {number}
 */
 // Time Complexity: O(n)
 // Space Complexity: O(1)

var halveArray = function(nums) {
  let total = nums.reduce((accumulator, currentValue) => accumulator + currentValue, 0)

  const expectedValue = total / 2;

  let counter = 0;

  while(expectedValue < total) {
    nums.sort((a, b) => b - a);

    nums[0] = nums[0] / 2;
    total -= nums[0];

    counter++;
  };


  return counter;
    
};


/*

5, 19, 8, 1 ===== total = 33;
reduce to 33 / 2 = 16.5 > reduced


3,8,20 ===== total = 31

reduce to 31 / 2 = 15.5 > reduced


1. divide max value by 2 and update answer.
      if answer less than expected value return total operations
   do the same operation until reach the expected value
   update the array each time divide the max value




*/


/**
 * @param {number[]} nums
 * @return {number}
 */
 // Time Complexity: O(n * n log n)
 // Space Complexity: O(1)
var halveArray = function(nums) {
  const maxQueue = new MaxPriorityQueue();
  console.log(maxQueue, 'hahahaah')
  let total = 0;

  for(const num of nums){
    total += num;
    maxQueue.enqueue(num);
  };

  const expected = total / 2;
  let counter = 0;

  while(total > expected) {
    counter++;
    const { element } = maxQueue.dequeue();
    const half = element / 2;

    total -= half;

    maxQueue.enqueue(half);
  };


return counter;

};


/*

5, 19, 8, 1 ===== total = 33;
reduce to 33 / 2 = 16.5 > reduced


3,8,20 ===== total = 31

reduce to 31 / 2 = 15.5 > reduced


1. divide max value by 2 and update answer.
      if answer less than expected value return total operations
   do the same operation until reach the expected value
   update the array each time divide the max value


var halveArray = function(nums) {
  let total = nums.reduce((accumulator, currentValue) => accumulator + currentValue, 0)

  const expectedValue = total / 2;

  let counter = 0;

  while(expectedValue < total) {
    nums.sort((a, b) => b - a);

    nums[0] = nums[0] / 2;
    total -= nums[0];

    counter++;
  };


  return counter;
    
};


*/
