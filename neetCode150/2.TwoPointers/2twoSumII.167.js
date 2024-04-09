/**
 * @param {number[]} numbers
 * @param {number} target
 * @return {number[]}
 */
// Time Complexity: O(n)
// Space Complexity: O(1)
// 4 minutes
var twoSum = function(numbers, target) {
  let leftIdx = 0
  let rightIdx = numbers.length - 1;

  while(leftIdx < rightIdx) {
    const sum = numbers[leftIdx] + numbers[rightIdx];

    if(sum === target) {
      return [leftIdx + 1, rightIdx + 1];
    }

    if(sum > target) {
      rightIdx--;
    } else {
      leftIdx++;
    };
  };


  /*
   compare two numbers sum with target
    sum === target
      return [leftIdx, rightIdx]
    sum > target
     rightIdx--;
    sum < target
     leftIdx++;
    

    do the above steps until reach leftIdx >= rightIdx

  */ 

  return []
    
};


/*



*/
