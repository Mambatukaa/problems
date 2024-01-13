// Time Complexity: O(n)
// Space Complexity: O(n)
const fn = (nums) => {
  const map = new Map();

  // initial value
  map.set(0, -1);

  let max = 0;
  let counter = 0;

  for(let i = 0; i < nums.length; i++) {
    nums[i] === 1 ? counter++ : counter--; 

    if(map.has(counter)) {
      max = Math.max(max, i - map.get(counter));
    } else {
        map.set(counter, i);
    };

  };

  console.log(map)

  return max;
}
const nums = [0, 1, 1, 0, 1, 1, 1, 0];

console.log(fn(nums));

/*

 */







