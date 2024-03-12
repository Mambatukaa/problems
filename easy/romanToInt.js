/**
 * @param {string} s
 * @return {number}
 */
var romanToInt = function(s) {
const algorism = new Map([
    ['CM', 900],
    ['CD', 400],
    ['XC', 90],
    ['XL', 40],
    ['IX', 9],
    ['IV', 4],
    ['M', 1000],
    ['D', 500],
    ['C', 100],
    ['L', 50],
    ['X', 10],
    ['V', 5],
    ['I', 1],
]);

  const arr = s.split("");
  const n = arr.length
  let answer = 0;

  for(let i = 0; i < n; i++) {
    const twoCharSymbol = arr[i] + arr[i + 1];
    const oneCharSymbol = arr[i];

    if(algorism.has(twoCharSymbol)) {
      answer += algorism.get(twoCharSymbol);
      i++;
    } else {
      answer += algorism.get(oneCharSymbol);
    }
  };

    
  return answer;
};


/*

IV = 4
VI = 6

XL = 40
XC 90

CD = 400
CM = 900

I             1
V             5
X             10
L             50
C             100
D             500
M             1000


1. Generate a map which has every possible roman values;
2. convert STRING to ARRAY
3. Use two pointers Left and Right
4. If left -> right is valid increase the right
    then after become invalid update the answer and update the pointer
  repeat until right pointer reach the end
5. return answer;

*/
