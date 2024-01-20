/**
 * @param {number[]} nums
 * @return {number}
 */
// Time Complexity: O(n)
// Space Complexity: O(n)
var maximumUniqueSubarray = function(nums) {
    const seen = new Set();
    let answer = 0;
    let l = 0;

    let curr = 0;

    for(let r = 0; r < nums.length; r++) {
        curr += nums[r];

        // shrink window
        // value is not unique
        while(seen.has(nums[r])) {
            seen.delete(nums[l]);
            curr -= nums[l];
            l++;
        };

        answer = Math.max(answer, curr);
        seen.add(nums[r]);
    };
    
    return answer;
};



/*
erasing value

          L
              R
nums = [4,2,4,5,6]
output: 17
Explan: [2, 4, 5, 6] unique elemented subarray

erased 6 [4,2]


1. Sliding window. Slide the window until subarray elements not unique. And update the answer.
2. To track uniqueness use set,
3. Shrink the window until subarray elements become unique again


TC: O(n)
SC: O(n)

*/
