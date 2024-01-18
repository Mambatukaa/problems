/**
 * @param {number[]} arr
 * @return {number}
 */
 // Time Complexity: O(1) // Max 500 elements
 // Space Complexity: O(n)
var findLuckyII = function(arr) {
    let answer = -1;    

    const map = new Map();

    for(const num of arr) {
        map.set(num, (map.get(num) || 0) + 1);
    };


    for([key, value] of map) {
        if(key === value) {
            answer = Math.max(answer, key);
        };
    };

    return answer;
};

 // Time Complexity: O(1) // Max 500 elements 
 // Space Complexity: O(n)
 // array is sorted this makes algorithm faster
var findLucky = function(arr) {
    const nums = new Array(501).fill(0);

    for(const num of arr) {
        nums[num]++;
    };


    for(let i = nums.length - 1; i > 0; i--) {
        if(i === nums[i]) {
            return i;
        }

    };

    return -1;
};

/*

const arr = [1,2,2,3,3,3]
output: 3;

answer = -1;
{
   1: 1,
   2: 2,
   3: 3
};

answer = 3;

Time Complexity: O(n)
Space Complexity: O(1) arr.length 1 <= n <= 500


*/
