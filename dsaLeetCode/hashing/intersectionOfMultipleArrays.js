// easy
// Time Complexity: O(n * m);
// Space Complexity: O(n)
const fn = () => {
 const map = new Map();
  
  for(const numList of nums) {

      for(const num of numList) {
          if(!map.has(num)) {
              map.set(num, 0);
          };

          map.set(num, map.get(num) + 1);
      };
  };

  const answer = [];

  for (let [key, value] of map) {
      if(value === nums.length) {
          answer.push(key);
      }
  }

  return answer.sort((a, b) => a - b);
};

const nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]];

console.log(fn(nums));
