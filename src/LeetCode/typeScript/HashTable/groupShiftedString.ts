function getHashKey(str: string) {
  let res = '';

  for(let i = 1; i < str.length; i++) {
   res += (str.charCodeAt(i) - str.charCodeAt(i - 1) + 26) % 26 + 'a'.charCodeAt(0); 
  }

  console.log(res, " response")


  return res;
}

// Time Complexity: O(NK)
// Space Complexity: O(N)

function groupStrings(strings: string[]) {
/*  if(strings.length <= 1) {
    return strings;
  } */
  
  const answer = new Map();

  for(let s of strings) {
    const key = getHashKey(s);

    if(!answer.has(key)) {
      answer.set(key, [s]);
      continue;
    }

    answer.get(key).push(s);
  }

  return [...answer.values()];

}

const strings = ["az", "za"]

console.log(groupStrings(strings));
