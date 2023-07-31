// Time Complexity: O(n)
// Space Complexity: O(1) because English alphabet contains 26 letters.
function firstUniqChar(s: string): number {
  const map = new Map();

  for(let i = 0; i < s.length; i++) {
    if(map.has(s[i])) {
      map.set(s[i], 1);

      continue;
    }

    map.set(s[i], 0);
  }

  for(let e of [...map]) {
    if(e[1] === 0) {
      return s.indexOf(e[0]);
    }
  }

  return -1;
}


console.log(firstUniqChar("aabb"));
