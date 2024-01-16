/**
 * @param {number[]} nums
 * @return {number}
 */
// Time Complexity: O(n * logn);
// Space Complexity: O(n)
var maximumSum = function(nums) {
    const map = new Map();
    let answer = -1;

    for(const num of nums) {
        const digitsSum = getDigitsSum(num);

        if(!map.has(digitsSum)) {
            map.set(digitsSum, []);
        };

        map.get(digitsSum).push(num);
    };

    for(const values of map.values()) {
        const n = values.length;

        if(n < 2) {
            continue;
        };

        values.sort((a, b) => a - b);

        answer = Math.max(answer, values[n - 1] + values[n - 2]);
    }


    return answer;
};

const getDigitsSum = (num) => {
    let answer = 0;

    while(num > 0) {
        answer += num % 10;
        num = Math.floor(num / 10);
    }

    return answer;
};



