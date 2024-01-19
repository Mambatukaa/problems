/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
// Time Complexity: O(n)
// Space Complexity: O(n)
var maxSubarrayLength = function(nums, k) {
    const map = new Map();
    let l = 0;
    let answer = 0;

    for(let r = 0; r < nums.length; r++) {
        const curr = nums[r];

        map.set(curr, (map.get(curr) || 0 ) + 1);

        // shrink window
        while(map.get(curr) > k) {
            const currElement = nums[l];
            map.set(currElement, map.get(currElement) - 1);

            l++;
        };

        answer = Math.max(answer, r - l + 1);
    };
    
    return answer;
};


/*

nums = [1, 2, 3, 1, 2, 3, 1, 2], k = 2
output: 6

[1, 2, 3, 1, 2, 3]
{
    1: 2,
    2: 2,
    3: 2

}

                          r
           l
nums = [1, 2, 3, 1, 2, 3, 1, 2], k = 2

1. 
{
    1: 2,
    2: 2,
    3: 2
};

Use sliding window approach and track count of the elements

Time Complexity: O(n)
Space Complexity: O(n) // If all value is unique


*/
