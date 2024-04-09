/**
 * @param {string[]} strs
 * @return {string[][]}
 */
// 13 minutes
var groupAnagrams = function(strs) {
  const map = new Map();

  for(const str of strs) {
    const sortedEl = str.split("").sort().join("");

    if(!map.has(sortedEl)) {
      map.set(sortedEl, [])
    };

    map.get(sortedEl).push(str);
  };

  return [...map.values()];

};


/*

strs = ["eat", "tea", "tan", "ate", "nat", "bat"];

output: [["eat", "tea", "ate"], ["nat", "tan", "bat"];


1. Solution using MAP.

if sorted element doesn't exists in map add the sorted element as a key and original element as a value.

if sorted element exists in map add unsorted element to the map.


Iterate through map values and push values to the answer;

return answer;

Time Complexity: O(n * s log s)
Space Complexity: O(n)

*/
