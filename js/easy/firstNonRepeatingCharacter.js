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

  for(let i = 0; i < string.length; i++) {
    if(value === 1) {
      return string.indexOf(key);
    }
  }

  return -1;
}

// Brute force
// Time Complexity: O(n^2)
// Space Complexity: O(1)
const firstNonRepeatingCharacterII = (string) => {
  for(let i = 0; i < string.length; i++) {
    let foundDuplication = false;

    for(let j = 0; j < string.length; j++) {
      if(string[j] === string[i] && i !== j) {
        foundDuplication = true;
      }
    }

    if(!foundDuplication) {
      return i;
    }
  }
  
  return -1;
}

console.log(firstNonRepeatingCharacterII("abcddbcaf")); // 1 index of b
