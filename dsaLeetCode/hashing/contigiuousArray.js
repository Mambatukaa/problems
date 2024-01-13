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

// Time Complexity: O(n)
// Space Complexity: O(n)
const fnII = (nums) => {
  const arr = new Array(nums.length * 2 + 1).fill(-2);

  arr[nums.length] = -1;

  let maxLength = 0;
  let count = 0;
  const n = nums.length;

  for(let i = 0; i < n; i++) {
    count = count + nums[i] === 0 ? -1 : 1;

    if(arr[count + n] >= -1) {
      maxLength = Math.max(maxLength, i - arr[count + n]);
    } else {
      arr[count + n] = i;
    };

  };

  console.log(arr, 'hahaahah')

  return maxLength;
};

const nums = [0, 1, 1, 0, 1, 1, 1, 0];

console.log(fnII(nums));






