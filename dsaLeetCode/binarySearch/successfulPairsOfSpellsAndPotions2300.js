/**
 * @param {number[]} spells
 * @param {number[]} potions
 * @param {number} success
 * @return {number[]}
 */
// TC: O((m * n) * log m) || O(m log m)
// SC: O(1)
var successfulPairs = function(spells, potions, success) {
  potions.sort((a, b) => a - b);
  const n = spells.length;
  const m = potions.length;

  const answer = [];

  for(const spell of spells) {
    let left = 0;
    let right = potions.length - 1; 

    while(left <= right) {
      const midIdx = Math.floor((left + right) / 2);
      const mid = potions[midIdx];
      const pair = spell * mid;

      if(pair >= success) {
        // go left
        right = midIdx - 1;
      } else {
        // go right
        left = midIdx + 1;
      };
    };

    console.log(left, 'hahhaha', right)

    answer.push(Math.abs(left - m));
  };
    
  return answer;
};


/*

Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
Output: [4,0,3]

Explanation:
- 0th spell: 5 * [1,2,3,4,5] = [5,10,15,20,25). 4 pairs are successful.
- 1st spell: 1 * [1,2,3,4,5] = [1,2,3,4,5]. 0 pairs are successful.
- 2nd spell: 3 * [1,2,3,4,5] = [3,6,2,12,15]. 3 pairs are successful.
Thus, [4,0,3] is returned.

*****************
spells[i] * potions[i] >= success SUCCESSFULY

spells array not sorted
potions array not sorted

NAIVE SOLUTION
1. Iterate through spells and also iterate through potions and check every pair 
      if pair is success increase the counter and push the counter to answer
2. It takes O(m * n) Time Complexity, O(n) Space Complexity:

n ==== spells.length;
m ==== potions.length;

BINARY SEARCH

1. Sort the potions
    TC: O(m log m); 
2. Iterate through spells and create pair with middle element of potions
  // and do the binary search until find the successful element
  // if found successfull update the counter = m - midIdx;
  // push to the answer array;


TC: O(n * log m) || O(m log m)
SC: O(1)


spells = [5, 1, 3] potions = [1,2,3,4,5] success = 7

  el = 5;

 l     m     r
 0     2     4
[1, 2, 3, 4, 5]

el * m = 15 > 7. go left

===============

 l  m  r     
 0  1  2     
[1, 2, 3, 4, 5]

el * m = 5 * 2 = 10 > 7



5 * 3 > 7 true
// go left
5 * 2 > 7 true
// go left
5 * 1 > 7
false 
found the right place
update answer




*/
