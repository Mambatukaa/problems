// Space complexity: O(1)
// Time complexity: O(n)
const lengthOfLongestSubArray = (nums, k) => {
  let leftIdx = 0;

  let max = 0;
  let currSum = 0;

  for(let rightIdx = 0; rightIdx < nums.length; rightIdx++) {
    // sliding window
    currSum += nums[rightIdx];

    // shrinking window
    while(currSum > k) {
      currSum -= nums[leftIdx];
      leftIdx++;
    };

    max = Math.max(max, rightIdx - leftIdx + 1);
}

  return max;
};

const nums = [3,2,0,3,1,1];
const k = 5;

console.log(lengthOfLongestSubArray(nums, k));


/*
function fn(arr):
    left = 0
    for (int right = 0; right < arr.length; right++):
        Do some logic to "add" element at arr[right] to window

        while WINDOW_IS_INVALID:
            Do some logic to "remove" element at arr[left] from window
            left++

        Do some logic to update the answer
*/
