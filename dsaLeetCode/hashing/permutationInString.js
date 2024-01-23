/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */


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

  return false;
};



// HashMaps
// Time limit Exceeded
// l1 be the length of string s1
// l2 be the length of string s1
// Time Complexity: O(l1 + 26l1(l2 - l1))
// Space Complexity: O(1) Hashmap contains at most 26 key value pairs

var checkInclusion = function(s1, s2) {
  if(s1.length > s2.length) {
    return false;
  };

  const s1Map = new Map();

  for(const ch of s1) {
    s1Map.set(ch, (s1Map.get(ch) || 0) + 1);
  };


  for(let i = 0; i < s2.length; i++) {
    const s2Map = new Map();

    for(let j = i; j < s1.length + i; j++) {
      s2Map.set(s2[j], (s2Map.get(s2[j]) || 0) + 1);
    };

    if(matches(s1Map, s2Map)) {
      return true;
    }

  };

  return false;
    
};

const matches = (map1, map2) => {
  for(const [key, value] of map1) {
    if(map2.get(key) !== value) {
      return false;
    };
  };

  return true;
};

// Time limit exceeded
// s1 s2 is lower case english letters
// l1 be the length of string s1
// l2 be the length of string s1
// Time Complexity: O(l1 + 26l1(l2 - l1))
// Space Complexity: O(1) Hashmap contains at most 26 key value pairs
const checkInclusionIII = (s1, s2) => {
  if(s1.length > s2.length) {
    return false;
  }

  const s1Arr = new Array(26).fill(0);

  for(let i = 0; i < s1.length; i++) {
    s1Arr[s1.charCodeAt(i) - "a".charCodeAt(0)]++;
  };

  console.log(s1Arr)

  for(let i = 0; i < s2.length; i++) {
    const s2Arr = new Array(26).fill(0);

    for(let j = i; j < i + s1.length; j++) {
     s2Arr[s2.charCodeAt(j) - "a".charCodeAt(0)]++;
    };

    if(arrMatches(s1Arr, s2Arr)) {
      return true;
    };

  };

  return false;
};

const arrMatches = (arr1, arr2) => {
  console.log(arr1, '===', arr2)

  for(let i = 0; i < 26; i++) {
    if(arr1[i] !== arr2[i]) {
      return false;
    }
  }

  return true;

};

// Sliding window
// Space complexity: O(1)
// Time complexity: O(1)
const checkInclusionIV = (s1, s2) => {
  if(s1.length > s2.length) {
    return false;
  }

  const s1Arr = new Array(26).fill(0)
  const s2Arr = new Array(26).fill(0)

  for(let i = 0; i < s1.length; i++) {
    s1Arr[s1[i].charCodeAt(0) - "a".charCodeAt(0)]++;
    s2Arr[s2[i].charCodeAt(0) - "a".charCodeAt(0)]++;
  };

  for(let i = 0; i < s2.length - s1.length; i++) {
    if(arrMatches(s1Arr, s2Arr)) {
      return true;
    };

    s2Arr[s2.charCodeAt(i + s1.length) - "a".charCodeAt(0)]++;
    s2Arr[s2.charCodeAt(i) - "a".charCodeAt(0)]--;
  };

  return arrMatches(s1Arr, s2Arr);
};


const s1 = "ba";
const s2 = "eidbaooo";

console.log(checkInclusionIV(s1, s2));
