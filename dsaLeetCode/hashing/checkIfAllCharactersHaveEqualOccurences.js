// Time Complexity: O(n)
// Space Complexity: O(n)
const fn = (s) => {
 const map = new Map();

  for(const letter of s) {
      if(!map.has(letter)) {
          map.set(letter, 0);
      };

      map.set(letter, map.get(letter) + 1);
  };

  let counter = 0;

  for(let [_key, value] of map) {
      // set first value as a counter
      if(counter === 0) {
          counter = value;
      };

      if(value !== counter) {
          return false;
      }
  }

  return true;

};

const s = "aabbcc";

// Time Complexity: O(n)
// Space Complexity: O(n)
var areOccurrencesEqual = function(s) {
    let counts = new Map();
    for (const c of s) {
        counts.set(c, (counts.get(c) || 0) + 1);
    }
    
    let frequencies = new Set();
    for (const val of counts.values()) {
        frequencies.add(val);
    }

    return frequencies.size == 1;
};

console.log(fn(s));
