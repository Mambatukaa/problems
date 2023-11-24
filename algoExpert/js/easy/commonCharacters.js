// Space Complexity: O(n)
// Time Complexity: O(n * m) // n = strings.length, m = longest string
const commonCharacters = (strings) => {
  const map = {};

  for(const string of strings) {
    const uniqueCharacters = new Set(string);

    for(const character of uniqueCharacters) {

      if(!map[character]) {
        map[character] = 0;
      }

      map[character]++;
    }
  }

  const finalCharacters = [];

  for(const [character, count] of Object.entries(map)) {
    if(count === strings.length) {
      finalCharacters.push(character);
    }
  }

  return finalCharacters;
}

const commonCharactersII = (strings) => {
  let smallestString = strings[0];

  // find smallest string
  for(const string of strings) {
    if(string.length < smallestString) {
      smallestString = string;
    }
  }

  // "abc"
  const potentialCommonString = new Set(smallestString);

  for(const string of strings) {
    const uniqueCharacters = new Set(string);

    for(const character of Array.from(potentialCommonString)) {
      if(!uniqueCharacters.has(character)) {
        potentialCommonString.delete(character);
      }
    }

  }

  return Array.from(potentialCommonString);
}



console.log(commonCharactersII(["abc", "bcd", "cbaccd"])); // => "bc"
