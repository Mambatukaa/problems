// Naive Brute Force approach
// Time Complexity: O(n^2);
// Space Complexity: O(n);
const semordnilap = (words) => {
  const answer = [];

  for(let i = 0; i < words.length; i++) {
    const currentWord = words[i];

    const output = [];

    for(let j = i + 1; j < words.length; j++) {
      const reversedWord = words[j].split("").reverse().join("");

      if(currentWord === reversedWord) {
        output.push(currentWord, words[j]);
      }

    }

    if(output.length) {
      answer.push(output);
    }
  }

  return answer;
}

// Time Complexity: O(n * m) // where n is the number of words
// Space Complexity: O(n * m) // m is the length of the longest word
const semordnilapII = (words) => {
  const answer = [];

  const set = new Set();

  for(const word of words) {
    const reversedWord = word.split("").reverse().join("");

    if(set.has(reversedWord)) answer.push([word, reversedWord]);
    else set.add(word);
  }

  return answer;
}

console.log(semordnilapII(["diaper", "abc", "test", "cba", "repaid"]));

