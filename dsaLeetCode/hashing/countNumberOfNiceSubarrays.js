// 
// Time Complexity: O(n)
// Space Complexity: O(n)
const fn = (nums, k) => {
  const map = new Map();
  map.set(0, 1);

  let oddPrefix = 0;

  // replace odd numbers by 1
  // replace even numbers by 1
  // because we will focus on the odd and even numbers
  for(let i = 0; i < nums.length; i++) {
    if(isOdd(nums[i])) {
      nums[i] = 1;
    } else {
      nums[i] = 0;
    };
  };


  let answer = 0;

  for(let i = 0; i < nums.length; i++) {
    if(nums[i] === 1) {
      oddPrefix += 1;
    };

    const diff = oddPrefix - k;

    answer += map.get(diff) || 0; 
    map.set(oddPrefix, (map.get(oddPrefix) || 0) + 1);
  };

  console.log(map)
  

  return answer;
};

const isOdd = (num) => {
  return num % 2 === 1;
}

const nums = [2,2,2,1,2,2,1,2,2,2];
const k = 2;

console.log(fn(nums, k));


/* 
 
  nums = [2,2,2,1,2,2,3,2,2,2]

  


 */
