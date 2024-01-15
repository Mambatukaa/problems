/**
 * @param {string[]} strs
 * @return {string[][]}
 */

// Naive solution
// Time Complexity: O(n * m logm) // m = string
// Space Complexity: O(n * m)
var groupAnagrams = function(strs) {
    const map = new Map();

    for(const str of strs) {
        const sortedStr = str.split("").sort().join("") ;

        if(!map.has(sortedStr)) {
            map.set(sortedStr, []);
        };

        map.get(sortedStr).push(str);
    };

    const answer = [];

    for(const group of map.values()) {
      answer.push(group);
    }

    return answer;
};

const strs = ["eat", "tea", "tan", "nat", "bat"];

console.log(groupAnagrams(strs));

