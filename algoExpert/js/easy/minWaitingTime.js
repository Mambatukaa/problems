// Time Complexity: O(nlogn)
// Space Complexity: O(1)
const minWaitingTime = (queries) => {
  let waitingTime = 0;
  let executionTime = 0;

  queries.sort((a, b) => a - b);

  for(let num of queries) {
    waitingTime += executionTime; 

    executionTime = executionTime + num;

  }

  return waitingTime;
}

// Time Complexity: O(nlogn)
// Space Complexity: O(1)
const minWaitingTimeII = (queries) => {
  queries.sort((a, b) => a - b);
  
  let waitingTime = 0;

  for(let i = 0; i < queries.length; i++) {
    // the total waiting queries
    let queriesLeft = queries.length - (i + 1);

    waitingTime += queries[i] * queriesLeft;


  }


  return waitingTime;
}

const queries = [1,2,3];

minWaitingTimeII(queries);

  // [1,2,3] ==> 0 + 1 + (1 + 2)
  // [3,2,1] ==> 0 + 3 + (3 + 2)
  // [3,2,1,2,6] => 0 + 3 + (3 + 2) + (3 + 2 + 1) + (3 + 2 + 1 + 2) = 22
  // [1,2,2,3,5] => 0 + 1 + (1 + 2) + (1 + 2 + 2) + (1 + 2 + 2 + 3) = 17
// 1 -> 4 -> 9 -> 17
//
//
//
//
// 1,2,3 => 0 + 1 + (1 + 2) + (1 + 2 + 3)
