/**
 * @param {number[]} nums
 * @return {number}
 */
var sumOfUnique = function(nums) {
    const map = new Map();

    for(const num of nums) {
        map.set(num, (map.get(num) || 0) + 1);
    };


    let uniqueSum = 0;

    for(const [key, value] of map) {
        // unique
        if(value === 1) {
            uniqueSum += key;
        };
    };
    
    return uniqueSum;
};




/*
 
 1. Brute force: O(n^2)
 2. Sort: TC: O(n logn)
 3. Map: TC: O(n) SC: O(n)


nums = [1,2,3,2];
output = 4 => 1 + 3 = 4;


1)
1. Brute force add currElement to the answer
2. To check duplication declare a variable named duplicated
3. TC: O(n^2) SC: O(1)

2)
1. map {} 
2. add elements to the map with counter
3. If elements already in the map increase the counter. 
4. If element count === 1 means unique
5. Iterate through maps and add unique elements to the answer
6 return answer;

TC: O(n)
SC: O(n)

*/

