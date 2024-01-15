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

// Time Complexity: O(n * m);
// Space Complexity: O(n * m)
const groupAnagramsII = (strs) => {
  const map = new Map();

  for(const str of strs) {
    let counter = 0;

    for(const letter of str) {
      counter+= letter.charCodeAt(0);
    };

    if(!map.has(counter)) {
      map.set(counter, []);
    };

    map.get(counter).push(str);

  };

  const answer = [];

  for(const value of map.values()) {
    answer.push(value);
  };

  return answer; 
};

const strs = ["eat", "tea", "tan", "nat", "bat"];

console.log(groupAnagramsII(strs));
