/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var subarraySum = function(nums, k) {
    let counter = 0;
    let answer = 0;
    let l = 0;

    for(let r = 0; r < nums.length; r++) {
        counter += nums[r];

        while(counter >= k && counter !== 0) {
            if(counter === k) {
                // update the answer
                answer++
            };

            counter -= nums[l];
            l++;
        };
    }

    return answer;
};


/*

nums = [1,2,3,4,5] k = 6 => [1,2,3].lenght = 3
output: 3

/ *
k = 6;

       l
       r
[1,2,3,4,5];

counter = 1 + 2 = 3 + 3 = 6 => update answer => shrink => 5 => 9 > k => shrink ;
answer = 0 => 3 =>; 
*/
// check counter === k update answer, 
// check counter > k shrink the substring

