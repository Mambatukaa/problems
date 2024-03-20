/**
 * @param {number[]} nums
 * @param {number[]} queries
 * @return {number[]}
 */
// TC: O(m * n + n log n)
// SC: O(1)
var answerQueriesII = function(nums, queries) {
  nums.sort((a, b) => a - b);

  const answer = [];

  for(const query of queries) {

    let counter = 0;
    let sum = 0;

    for(const num of nums) {
      sum += num;

      if(sum > query) {
        break;
      };

      counter++;
    };

    answer.push(counter);

  };

  return answer;
    
};


// Prefix sum and binary search
// Time Complexity: O(m * log n + n log n)
// Space Complexity: O(1)
var answerQueries = function(nums,queries) {
    let res = [];

    nums.sort((a,b)=>a-b);

    // prefix sum
    for (let i = 1; i<nums.length; i++) {
        nums[i] += nums[i-1];
    };

    let binarySearch = function(arr,num) {
        let left  = 0;
        let right = arr.length - 1;

        while(left <= right) {
          let mid = Math.floor((left+right)/2);

          if(arr[mid] === num) {
            return mid + 1;
          };

          if (arr[mid] > num) {
              right = mid - 1;
          } else {
              left = mid + 1;
          }
        }

        return left;
    };

    for (let q of queries) {
        res.push(binarySearch(nums,q));
    };
    
    return res;
};


/*
nums = [4, 5, 2, 1], // unSorted
queries = [3, 10, 21]; // unSorted

1. Try to create max subsequence using my nums which fits queries[i];

2. nums = [1, 2, 4, 5]
queries = [3, 10, 21]

NAIVE
1. Sort the nums to start from smallest elements.
2. Iterate through queries  
    Iterate through nums and sum up nums until reach the query limit
    Once reaches the query limit add counter to answer array;

TC: O(n * m)
SC: O(1)


PREFIX SUM

nums = [1,2,4,5] =====> [1, 3, 7, 12]



*/
