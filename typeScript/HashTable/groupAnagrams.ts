// Using sort
// Time Complexity: O(N * K logK); K is the maximum length of a string in strs. 
// Space Complexity: O(NK), the totla information content stored in ans.

function anagrams(strs: string[]) {
  const answer = new Map();

  for(let s of strs) {
    const sortedStr = s.split('').sort().toString();

    if(!answer.has(sortedStr)) {
      answer.set(sortedStr, [s]);
      continue;
    } 

    answer.get(sortedStr).push(s);
  }


  const response = [...answer.values()];

  console.log(response);

  return response;
}


// Time Complexity: O(NK) 
// Space Complexity: O(NK)
function anagramsCount(strs: string[]) {
  const answer = new Map();

  for(let s of strs) {
    const count = new Array(26);
    count.fill(0);

    for(let e of s) {
      count[e.charCodeAt(0) - 'a'.charCodeAt(0)]++; 
    }

    if(!answer.has(count.toString())) {
      answer.set(count.toString(), [s]);

      continue;
    } 

    answer.get(count.toString()).push(s);
  }

  return [...answer.values()];
}


console.log(anagramsCount(["eat", "tea", "ate", "bat"]));
