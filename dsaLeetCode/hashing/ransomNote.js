/**
 * @param {string} ransomNote
 * @param {string} magazine
 * @return {boolean}
 */
// TC: O(n + m)
// SC: O(m)
var canConstruct = function(ransomNote, magazine) {
    const map = new Map();

    for(const ch of magazine) {
        map.set(ch, (map.get(ch) || 0) + 1);
    }


    for(const ch of ransomNote) {
        if(!map.has(ch)) {
            return false;
        } 
        
        map.set(ch, map.get(ch) - 1);

        if(map.get(ch) === 0) {
            map.delete(ch);
        }
        
    }


    return true;
};


// Time Complexity: O(n + m)
// Space Complexity: O(1)
var canConstructII = function(ransomNote, magazine) {
    const map = new Array(26).fill(0);

    for(const ch of magazine) {
      const idx = ch.charCodeAt(0);

      map[idx - "a".charCodeAt(0)]++;
    }

    for(const ch of ransomNote) {
      const idx = ch.charCodeAt(0);

      if(map[idx - "a".charCodeAt(0)] === 0) {
        return false;
      }

      map[idx - "a".charCodeAt(0)]--;
    }



    return true;
};

console.log(canConstructII("abc", "bc"));


/*

use ransomNote using magazine

1. map
2. iterate through magazine and store characters with count on map
3. iterate through ransomNote and check characters from map and found decrease if not found return false

TC: O(n + m)
SC: O(m)


*/
