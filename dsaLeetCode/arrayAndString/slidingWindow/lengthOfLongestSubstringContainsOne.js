// Time Complexity: O(n)
// Space Complexity: O(1)
const solution = (s) => {
  let leftIdx = 0;
  let answer = 0;
  let curr = 0;

  for(let rightIdx = 0; rightIdx < s.length; rightIdx++) {
    // sliding window
    if(s[rightIdx] === "0") {
      curr++;
    };

    // shrinking window
    while(curr > 1) {
      if(s[leftIdx] === '0') {
        curr--;
      };

      leftIdx++;
    };

    answer = Math.max(answer, rightIdx - leftIdx + 1);
  };

  return answer;

};

const s = '1111111110';

console.log(solution(s));
