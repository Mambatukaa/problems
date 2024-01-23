/**
 * @param {string} pattern
 * @param {string} s
 * @return {boolean}
 */
// Time Complexity: O(n)
// Space Complexity: O(n + m)
var wordPattern = function(pattern, s) {
    const words = s.split(" ");
    const pMap = new Map(); 
    const seen = new Set();

    if(words.length !== pattern.length) {
        return false;
    }

    for(let i = 0; i < pattern.length; i++) {

        if(pMap.has(pattern[i])) {
            if(pMap.get(pattern[i]) !== words[i]) {
                return false;
            };
        } else {
            if(seen.has(words[i])) {
                return false;
            }

            seen.add(words[i]);
            pMap.set(pattern[i], words[i]);
        }


    };

    return true;
    
};

const pattern = "aaa";
const s = "dog dog cat";

console.log(wordPattern(pattern, s));

