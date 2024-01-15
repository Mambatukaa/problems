/**
 * @param {string[]} strs
 * @return {string[][]}
 */

// Naive solution
// Time Complexity: O(n * n logn)
// Space Complexity: O(n)
var groupAnagrams = function(strs) {
    const map = new Map();
    let idx = 0;

    for(const str of strs) {
        const sortedStr = str.split("").sort().join("") ;

        if(!map.has(sortedStr)) {
            map.set(sortedStr, idx);
            idx++;
        };
    };

    const answer = [];

    for(const str of strs) {
        const sortedStr = str.split("").sort().join("") ;
        const key = map.get(sortedStr);

        if(!answer[key]) {
            answer[key] = [str];
        } else {
            answer[key].push(str);
        }

    };

    return answer;
};

const strs = ["eat", "tea", "tan", "nat", "bat"];

console.log(groupAnagrams(strs));

