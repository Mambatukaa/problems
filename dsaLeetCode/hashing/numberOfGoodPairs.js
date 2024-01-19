/**
 * @param {number[]} nums
 * @return {number}
 */
 // Time Complexity: O(n)
 // Space Complexity: O(1) // 100 elements ???
var numIdenticalPairsII = function(nums) {
    const map = new Map();
    let answer = 0;

    for(const num of nums) {
        if(map.has(num)) {
            answer += map.get(num);
        };

        map.set(num, (map.get(num) || 0) + 1);
    };

    return answer;
    
};

 // Time Complexity: O(n)
 // Space Complexity: O(1) // 100 elements
var numIdenticalPairs = function(nums) {
    const arr = new Array(101).fill(0);
    let answer = 0;

    for(const num of nums) {
       answer += arr[num]++;
    };

    return answer;
    
};



/*
        0 1 2 3 4 5
nums = [1,2,3,1,1,3];
output: 4

counter 0 => map.has(1) => counter += map value => 1 =>  
map  = {
    1: 2,
    2: 1,
    3: 1
}


(1,1), (1,1)  (1,1)  (3,3)
(0,3), (0,4), (3,4), (2,5)

i = idx;
j = idx;

nums[i] === nums[j] good pairs
i < j



1. Declare the variable counter = 0;
2. Iterate through arrays
3. Declare set named seen
4. Add elements to the map
5. If element has in map increase the counter by count
return counter;





 */
