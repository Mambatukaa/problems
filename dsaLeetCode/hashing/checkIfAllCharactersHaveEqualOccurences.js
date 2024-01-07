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

console.log(fn(s));
