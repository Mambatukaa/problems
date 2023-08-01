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



anagrams(["eat", "tea", "ate", "bat"]);
