// Time Complexity: O(n)
// Space Complexity: O(n)

function twoSum(nums: number[], target: number): number[] {
  const map = new Map();

  for(let i = 0; i < nums.length; i++) {
    const diff = target - nums[i];

    if(map.has(diff)) {
      return [map.get(diff), i];
    }

    map.set(nums[i], i);
  }

  return [];
}


console.log(twoSum([7,4,8,2], 9));

