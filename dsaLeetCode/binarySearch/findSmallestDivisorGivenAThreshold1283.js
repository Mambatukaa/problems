/**
 * @param {number[]} nums
 * @param {number} threshold
 * @return {number}
 */
 // Time Complexity: O(n * log k)
 // Space Complexity: O(1)
var smallestDivisor = function(nums, threshold) {

  const check = (k) => {
    let total = 0;

    for(const num of nums) {
      total += Math.ceil(num / k);
    };

    return total <= threshold;
  };


  let left = 1;
  let right = Math.max(...nums);


  while(left <= right) {
    const mid = Math.floor((left + right) / 2);

    if(check(mid)) {
      // try with lower element
      right = mid - 1;
    } else {
      // try with higher element
      left = mid + 1;
    }
  }

  return left;
    
};



/*

nums = [1,2,5,9], threshold = 6;

Output: smallest divisor (5)

1. If I division all elements by 5 and their sum will be 6;
2. 1 / 5 + 2 / 5 + 5 / 5 + 9 / 5 ====== 1 + 1 + 1 + 2 = 5;
3. (6) === 1 / 6 + 2 / 6 + 5 / 6 + 9 / 6 ========= 1 + 1 + 1 + 2 = 5;

NAIVE SOLUTION 
try to division starts from max element and compare with threshold.


BINARY SEARCH, GREEDY function

1. Check mid element is successful division 
    If success
      decrease mid element
    else
      increase mid element
    because we are trying to find min
2. Start left = 1, right = max element of an array


TC: O(n * log k)
SC: O(1)


*/
