/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */

// brute force
// TC: O(n)
// SC: O(n)
// Time limit exceeded
var checkInclusion = function(s1, s2) {
    const map = new Map();

    for(const ch of s1) {
        map.set(ch, (map.get(ch) || 0) + 1);
    };

    console.log(map)

    for(let i = 0; i < s2.length; i++) {
        const newMap = new Map(map);

        if(!newMap.has(s2[i])) {
            continue;
        };

        newMap.set(s2[i], map.get(s2[i]) - 1);

        if(newMap.get(s2[i]) === 0) {
            newMap.delete(s2[i]);
        };

        
        if(newMap.size === 0) {
            return true;
        }

        for(let j = i + 1; j < s2.length; j++) {
            if(!newMap.has(s2[j])) {
                console.log('----------------------')
                break;
            };

        newMap.set(s2[j], newMap.get(s2[j]) - 1);

        if(newMap.get(s2[j]) === 0) {
            newMap.delete(s2[j]);
        };

        console.log(newMap, '------', s2[j])

        if(newMap.size === 0) {
            return true;
        }


        };


    };

    return false;
    
};

// sorting
// Time Limit Exceeded
// Time Complexity: O(l1 log(l1) + (l2 - l1) l1 log(l1));
// Space Complexity: O(l1)
const checkInclusionII = (s1, s2) => {
 const sortedS1 = s1.split("").sort().join("");

  for(let i = 0; i < s2.length; i++) {
    if(sortedS1 === s2.substring(i, sortedS1.length + i).split("").sort().join("")) {
      return true;
    };
  };

  return false;};

const s1 = "ba";
const s2 = "eidbaooo";

console.log(checkInclusionII(s1, s2));
