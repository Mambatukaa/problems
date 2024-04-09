/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
// 7 Minutes
var isAnagram = function(s, t) {
  if(s.length !== t.length) {
    return false;
  };

  const charArray = new Array(26).fill(0);

  for(let i = 0; i < s.length; i++) {
    charArray[s.charCodeAt(i) - 'a'.charCodeAt(0)]++;
    charArray[t.charCodeAt(i) - 'a'.charCodeAt(0)]--;
  };

  return charArray.every((count) => count === 0)
};


/*

1. Sort and compare s and t's characters.
  Time Complexity: O(s log s + t log t)
  Space Complexity: O(1)

2. Hashtable (MAP)
  Add s characters to the map and count.

  Iterate through t and remove t's character from MAP. 

  After iteration if map is empty return true otherwise return false;

  Time Complexity: O(s + n)
  Space Complexity: O(s)

3. Use ARRAY as a MAP. Because characters are only letters;

  Time Complexity: O(s + n);
  Space Complexity: O(1);
*/
