// Time Complexity: O(n)
// Space Complexity: O(n)
const fn = (nums, target) => {
  const map = new Map();

  for(let i = 0; i < nums.length; i++) {
    const diff = target - nums[i];

    if(map.has(diff)) {
      return [i, map.get(diff)];
    };

    map.set(nums[i], i);
  };

  return [];
};

const nums = [0, 5, 2, 7, 10, 3, 9];
const target = 8;

console.log(fn(nums, target));
