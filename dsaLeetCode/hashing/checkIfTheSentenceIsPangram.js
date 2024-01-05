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


/*
 
class Solution {
    public boolean checkIfPangram(String sentence) {
        // We iterate over 'sentence' for 26 times, one for each letter 'currChar'.
        for (int i = 0; i < 26; ++i) {
            char currChar = (char)('a' + i);

            // If 'sentence' doesn't contain currChar, it is not a pangram.
            if (sentence.indexOf(currChar) == -1)
                return false;
        }
        
        // If we manage to find all 26 letters, it is a pangram.
        return true;
    }
}
 */
