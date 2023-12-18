// Space Complexity: O(1)
// Time Complexity: O(n)
const fn = (nums, k) => {
  let left = 0;
  let answer = 0;
  let curr = 0;

  for(let right = 0; right < nums.length; right++) {
    if(nums[right] === 0) {
      curr++;
    };

    // shrink
    while(curr > k) {
      if(nums[left] === 0) curr--;

      left++;
    };

    answer = Math.max(answer, right - left + 1);
  };


  return answer
};


const nums = [1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0];
const k = 2;

console.log(fn(nums, k));
