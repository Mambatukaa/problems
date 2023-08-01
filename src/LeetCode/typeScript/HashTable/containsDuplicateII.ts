// Time complexity: O(n)
// Space complexity: O(n)

function containsNearbyDuplicate(nums: number[], k: number): boolean {
  const map = new Map();

  for(let i = 0; i < nums.length; i++) {
    const currNum = nums[i];

    if(map.has(currNum) && i - map.get(currNum) <= k) {
      return true;
    }

    map.set(currNum, i);
  }

  return false;
}

console.log(containsNearbyDuplicate([1,2,3,4,5,1, 1], 3));
