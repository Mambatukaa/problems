// find the number of subarrays that have sum less than k

const fn = (nums, k) => {
  let curr = 0;
  let counter = 0;

  let l = 0;

  // sliding window
  
  for(let r = 0; r < nums.length; r++) {
    curr += nums[r];
    
    // if its not fit in constraint shrink the window
    while(curr >= k) {
      curr -= nums[l];
      l++;
    };

    // valid
    counter += r - l + 1;
  };

  return counter;
};

        
const nums = [1,3,2,5,1,3]
const k = 7;

/*
                   r
                 l
 nums = [1,3,2,5,1,3] k = 7

 curr < k (7)

   l 0 0 0 0  1  2  3 3 3 4 4 
   r 0 1 2 3  3  3  3 4 5 5 6
lNum 1 1 1 1  3  2  5 5 5 1 ---- end
rNum 1 3 2 5  5  5  5 1 3 3
curr 1 4 6 11 10 7  5 6 9 4
 val t t t f  f  f  t t f t
 ctr 1 3 6 -  -  -  7 9 - 11

 ctr += r - l + 1


 return 11;

 Time Complexity: O(n)
 Space Complexity: O(1)
 */






// number of subarrays that sum equals to k
const fnII = (nums, k) => {
  const map = new Map();
  map.set(0, 1);

  let prefix = 0;
  let answer = 0;

  for(const num of nums) {
    prefix += num;

    answer += map.get(prefix - k) || 0;
    // the reason increasing the prefix value is because we have negative numbers
    map.set(prefix, (map.get(prefix) || 0) + 1);
  };

  console.log(map)

  return answer;
};

const arr = [1,2,1,2,1];
const sum = 3
//  0,1    1,3    2,3    3,4
// [1,2], [2,1], [1,2], [2,1]
//
console.log(fnII(arr, sum));
