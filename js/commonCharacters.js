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



console.log(commonCharacters(["abc", "bcd", "cbaccd"])); // => "bc"
