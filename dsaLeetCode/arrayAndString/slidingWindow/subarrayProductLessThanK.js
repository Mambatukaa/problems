// brute force
const arrayProduct = (nums, k) => {
  let counter = left = 0;
  let sum = 1;

  while(left < nums.length) {
    let right = left;

    if(nums[left] < k) {
      counter++;
    };

    sum *= nums[left];

    while(right < nums.length) {
      right++;

      sum *= nums[right];

      if(sum < k) {
        counter++;
      }     

    };

    sum = 1;
    left++;
  };

  return counter;
};

// Space Complexity: O(1)
// Time Complexity: O(n)
const arrayProductSum = (nums, k) => {
  if(k <= 1) {
    return 0;
  };

  let left = 0;
  let curr = 1;
  let answer = 0;

  for(let right = 0; right < nums.length; right++) {
    // slide
    curr = curr * nums[right];

    while(curr >= k) {
      //shrink
      curr = curr / nums[left];
      left++;
    };

    console.log(curr,'hahhaha')

    answer += right - left + 1;
  };

  return answer;
};


const k = 1;
const nums = [10, 5, 2, 6];

console.log(arrayProductSum(nums, k));
