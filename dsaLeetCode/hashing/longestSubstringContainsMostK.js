// 1. track the characters in range
// 2. if our range reach the limit which is k update the answer shrink the window 
// 3. else slide the window
//
// Time Complexity: O(n)
// Space Complexity: O(k)
const fn = (s, k) => {
  let answer = 0;
  const map = new Map();
  let l = 0;

  for(let r = 0; r < s.length; r++) {
    const char = s[r];

    if(!map.has(char)) {
      map.set(char, 1);
    } else {
      map.set(char, map.get(char) + 1)
    };


    // shrink
    while(map.size > k) {
      const currChar = string[l];


      if(map.get(currChar) === 0) {
          map.delete(currChar);
      } else {
        map.set(currChar, map.get(currChar) - 1);
      };

      l++;
    };
    console.log(map)

    answer = Math.max(r - l + 1, answer);
  };

  return answer;
};

// Time Complexity: O(n)
// Space Complexity: O(k)
const findLongestSubstring = (s, k) => {
  const counts = new Map();
  let left = 0, ans = 0;

  for(let right = 0; right < s.length; right++) {
    counts.set(s[right], (counts.get(s[right]) || 0) + 1);

    console.log(counts);
    // shrinking
    while(counts.size > k) {
      counts.set(s[left], counts.get(s[left]) - 1);

      if(counts.get(s[left]) === 0) {
        counts.delete(s[left]);
      };

      left++;
    };

    ans = Math.max(right - left + 1, ans);
  };

  return ans;
};

const string = "eceba";
const k = 2;

console.log(findLongestSubstring(string, k));
