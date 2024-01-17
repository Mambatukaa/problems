/**
 * @param {number[]} nums
 * @return {number}
 */
// Time Complexity: O(n)
// Space Complexity: O(1) only 100 elements
var maxFrequencyElementsII = function(nums) {
    const map = new Map();
    let maxFrequency = 0;

    for(const num of nums) {
        map.set(num, (map.get(num) || 0) + 1);

        const value = map.get(num);

        maxFrequency = maxFrequency  < value ? value : maxFrequency  ;
    };

    let answer = 0;

    for(const value of map.values()) {
        if(value === maxFrequency) {
            answer+= value;
        };
    };

    return answer;
};

// Time Complexity: O(n)
// Space Complexity: O(1) only 100 elements
var maxFrequencyElements = function(nums) {
    const arr = new Array(101).fill(0);
    let maxFrequency = 0;

    for(const num of nums) {
        arr[num]++;
        
        const value = arr[num];

        maxFrequency = maxFrequency  < value ? value : maxFrequency  ;
    };

    let answer = 0;

    console.log(maxFrequency, )

    for(let i = 1; i < 101; i++) {
        if(arr[i] === maxFrequency) {
            answer += maxFrequency;
        }
    };



    return answer;
};


/*

frequency of an element is the number of occurances that element in the array

nums = [1,2,2,3,1,4];
Output = 4;

{
    1: 2,
    2: 2,
    3: 1,
    4: 1
}

1. set elements with counter on the map
2. find max frequency
3. answer = 0;
4. iterate through maps and value === maxFrequency answer+= value;
5. return answer;

TC: O(n)
SC: O(n)



nums = [1,2,3,4,5]
output = 5

{
    1: 1,
    2: 1,
    3: 1,
    4: 1,
    5: 1
}

frequency: 1
max: 5



*/
