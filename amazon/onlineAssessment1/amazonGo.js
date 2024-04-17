import {
  MinPriorityQueue,
} from '@datastructures-js/priority-queue';

// Time Complexity: O(m * n log n);
// Space Complexity: O(n);

const getMinimumCostII = (n, a, b, m) => {
  const calculate = (i, j) => {
    return a[i] + (j - 1) * b[i];
  };

  const minHeap = new MinPriorityQueue();
  let j = 1;
  let total = 0;

  // add calculated item to heap 
  // when calculated item reaches the limit get the min item and increase the total
  // when heap become empty increase the j and calculate the items again
  // Retreat the above step until m reaches the 0 which is we purchased all data in min price;
  
  while(m > 0) {

    // calculate all values in current j
    for(let i = 0; i < n; i++) {
      const price = calculate(i, j);

      minHeap.enqueue(price);
    };

    while(minHeap.size()) {
      const min = minHeap.dequeue();
      console.log(min, m, j )
      total += min

      m--;

      if(m === 0) {
        break;
      }
    };

    j++;
  }

  return total;
};

// Time Complexity: O(m * n log n);
// Space Complexity: O(n);
const getMinimumCost = (n, a, b, m) => {

  const calculate = (i, j) => {
    return a[i] + (j - 1) * b[i];
  };


  const arr = [];
  let total = 0;
  let j = 1;


  while(m > 0) {

    // calculate values with current j
    
    for(let i = 0; i < n; i++) {
      arr.push(calculate(i, j));
    };

    arr.sort((a, b) => a - b);

    while(arr.length) {

      total += arr.shift();
      m--;

      if(m === 0) {
        break;
      };
    };

    j++;
  };

  console.log(total)

  return total;
};

const n = 3;
const a = [2,1,1];
const b = [1,2,3];
const m = 4;


getMinimumCost(n, a, b, m)

/*
const pairs = [[2,1], [1,3], [1, 2]];

pairs.sort((a, b) => {
 if(a[0] === b[0]) {
    return a[1] - b[1]
 } else {
    return a[0] - b[0]}
})

console.log(pairs, '=====')
*/

/*
 
Example

  Given n = 3, a = [2, 1, 1], b = [1, 2, 3], m = 4


The optimal types to buy are

  • Choose type i = 1. This is the first purchase of this type, so j = 1. This item
      costs a[1] + (j - 1) * b(i] = 1 + (1 - 1) * 2 = 1.

  • Choose type i = 2. This is the first purchase of this type, so j = 1. This item
      costs 1 + (1 - 1) * 3 = 1.

  • Choose type i = 0. This is the first purchase of this type, so j = 1. This item
      costs 2 + (1 - 1) * 1 = 2.

  • When a second item of any type is purchased, j = 2. The cost of the item for
      each type will be:

  • Type i = 0, costs a(0] + (i - 1) * b[0] = 2 + (2 - 1) * 1 = 3
  • Type i = 1, costs 1 + 1 * 2 = 3
  • Type i = 2, costs 1 + 1 * 3 = 4
  • Choose either the first or second type since they cost the least.

  The total cost to purchase is 1 + 1 + 2 + 3 = 7.


Function Description
  Complete the function getMinimumCost in the editor below.

  getMinimumCost has the following parameters:

  int a[n]: an array of integers
  int b[n]: an array of integers
  m: the number of items to purchase.




  Given n = 3, a = [2, 1, 1], b = [1, 2, 3], m = 4

  J = 1;
    a sorted order will be optimal.
  J > 1;
    b sorted order will be optimal

  FORMULA = a[i] + (j - 1) * b[i];


  Create pair with a,b ====> pair = [[2, 1], [1, 2], [1, 3]];

  sort the pair by first element; IF ELEMENTS ARE EQUAL COMPARE SECOND ELEMENTS and SORT

    j = 1;

    iterate through pair and calculate optimal costs using formula.
    DECREASE M


  since j > 1
    reverse sorted order will be the optimal. sort it by a[1] IF ITEMS ARE EQUAL COMPARE FIRST ELEMENTS AND SORT



    n = 3;

    a = [100, 1, 1];
    b = [1, 2, 3];
    m = 5;


    j = 1;
     F: a[i] + (1 - 1) * b[i]

      i = 1, 
        1 + (1 - 1) * 2 = 1; m = 4;
      i = 2,
        1 + 0 = 1; m = 3;
      i = 0,
        100 + 0 = 100; m = 2;


    j = 2;



    USE MIN HEAP
      Calculate price on j's and add to the heap. Get min value from heap and decrease the m and increase the total product





    NAIVE APPROACH
      Create possible values on each j and sort and calculate total;
      Until m reaches 0;
      
      Time Complexity: O(n * n log n);

      
      







    

 


 */
