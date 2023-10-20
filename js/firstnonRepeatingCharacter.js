// Time Complexity: O(n)
// Space Complexity: O(1) // because hashTable contains maximum of 26 characters
const firstNonRepeatingCharacter = (string) => {
  const map = {};

  for(const letter of string) {
    if(!map[letter]) {
      map[letter] = 0;
    }

    map[letter]++;
  }

  for(const [key, value] of Object.entries(map)) {
    if(value === 1) {
      return string.indexOf(key);
    }
  }

  return -1;
}


console.log(firstNonRepeatingCharacter("abcddbcaf")); // 1 index of b
