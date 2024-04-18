/**
 * @param {string} s
 * @return {number}
 */


// 5 minutes
// Time Complexity: O(n)
// Space Complexity: O(n)

var lengthOfLongestSubstring = function(s) {
  // iteration will be faster
  const arr = s.split("");
  const n = arr.length;
  let res = 0;
  let left = 0;

  // check repetition;
  const seen = new Set();

  for(let right = 0; right < n; right++) {

    while(seen.has(arr[right])) {
      seen.delete(arr[left]);

      left++;
    };

    seen.add(arr[right]);

    res = Math.max(res, right - left + 1);
  };

  return res;
};



/*

longest substring without repeating characters






*/
