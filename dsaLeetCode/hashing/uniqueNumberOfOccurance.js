/**
 * @param {number[]} arr
 * @return {boolean}
 */
// Space Complexity: O(n)
// Time Complexity: O(n)
var uniqueOccurrencesII = function(arr) {
    const map = new Map();

    for(const num of arr) {
        map.set(num, (map.get(num) || 0) + 1);
    };

    const set = new Set();

    for(const value of map.values()) {
        if(set.has(value)) {
            return false;
        };

        set.add(value);
    }
    
    return true;
};

// Space Complexity: O(n)
// Time Complexity: O(n)
var uniqueOccurrences = function(arr) {
    const nums = new Array(2001).fill(0);

    for(const num of arr) {
        nums[num + 1000]++;
    };

    const set = new Set();

    for(const value of nums) {
        if(value === 0) {
            continue;
        }

        if(set.has(value)) {
            return false;
        };

        set.add(value);
    }
    
    return true;
};


/*
1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000

arr = [1, 2, 2, 1, 1, 3]
output = true;

{
    1: 3,
    2: 2,
    3: 1
}

every values are unique return true otherwise return false;


arr = [1,2];
output = false;

{
    1: 1,
    2: 1
}

1. [1, 2, 2, 1, 1, 3] 
    map = {
        1: 3,
        2: 2,
        3: 1
    };

    generate an set using all values

    [3,2,1]

    if(set.has(value)) return false;

    return true


// Time Complexity: O(n)
// Space Complexity: O(n)

*/


