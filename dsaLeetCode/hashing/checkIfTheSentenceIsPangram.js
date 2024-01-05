// Time Complexity: O(n)
// Space Complexity: O(1) // only 26 letters
const fn = (sentence) => {
  const set = new Set();

  for(const letter of sentence) {
      if(set.has(letter)) {
          continue;
      };

      set.add(letter);
  };

  console.log(set)

  return set.size === 26;
};


const sentence = "thequickbrownfoxjumpsoverthelazydog";

console.log(fn(sentence));
