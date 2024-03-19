/**
 * @param {number[]} people
 * @param {number} limit
 * @return {number}
 */
 // It works because at most 2 people can sit on 1 boat.
 // Time Complexity: O(n log n) // sort
 // Space Complexity: O(1) // some sorting algorithm takes O(n)
var numRescueBoats = function(people, limit) {
  // 2 pointers
  let leftIdx = 0;
  let rightIdx = people.length - 1;
  people.sort((a, b) => a - b);

  let counter = 0;

  while(leftIdx <= rightIdx) {
    const weight = people[leftIdx] + people[rightIdx]; 

    if(weight <= limit) {
      leftIdx++;
      rightIdx--;
    } else {
      rightIdx--;
    }

    counter++;
  };

  return counter;
};


/*
Find how many boat need to carry people.

Input: 
  people = [1, 2], limit = 3
Output: 1
Expl:
  1 boat (1, 2);


Input:
  people = [3, 2, 2, 1], limit = 3;
Output: 3
Expl:
  3 boats (1, 2), (2), (3)


  Try to sit max with min

  limit = 10;

  [9, 5, 4, 1, 10, 8]

  l         r
  l       r
    l   r
    l r

  1,4,5,8,9,10

  (9, 1), (10), (8), (5, 9) === 4

  Try to sit max with min

  if(max + min <= limit) {
    leftPointer++;
    righttPointer++;
  } else {
    rightPointer--;
  };

  counter++;

  TC: O(n);
  SC: O(n);

*/
