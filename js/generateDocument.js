// Time Complexity: O(n + m);
// Space Complexity: O(n + m);
const generateDocument = (characters, document) => {
  if(document.length > characters.length) {
    return false;
  }

  const characterMap = {};
  for(const character of characters) {
    if(!characterMap[character]) {
      characterMap[character] = 0;
    }

    characterMap[character]++;
  }

  const documentMap = {};

  for(const doc of document) {
    if(!documentMap[doc]) {
      documentMap[doc] = 0;
    }

    documentMap[doc]++;
  }

  for(const [key, value] of Object.entries(documentMap)) {

    if(!characterMap[key]) {
      return false;
    }

    if(characterMap[key] < value) {
      return false;
    }
  }

  return true;
}

// Time Complexity: O(n + m);
// Space Complexity: O(c); c = unique characters in the characters string
const generateDocumentII = (characters, document) => {
  const characterMap = {};

  for(const character of characters) {
    if(!characterMap[character]) {
      characterMap[character] = 0;
    }

    characterMap[character]++;
  }

  for(const letter of document) {
    if(!(letter in characterMap) || characterMap[letter] === 0) {
      return false;
    }

    characterMap[letter]--;
  }

  return true;
}

// Brute force
// Time Complexity: O(c * (n + m))
// Space Complexity: O(c) c - unique characters
const generateDocumentIII = (characters, document) => {
  const alreadyCounter = new Set();

  for(const character of document) {
    if(alreadyCounter.has(character)) continue;

    const documentFrequency = countCharacterFrequency(character, document)
    const charactersFrequency = countCharacterFrequency(character, characters)

    if(documentFrequency > charactersFrequency) {
      return false;
    }

    alreadyCounter.add(character);
  }

  return true
}

const countCharacterFrequency = (character, target) => {
  let frequency = 0;

  for(const char of target) {
    if(char === character) frequency++;
  }

  return frequency;
}

console.log(generateDocument("hello1ww0  rld", "hellowrld"));
