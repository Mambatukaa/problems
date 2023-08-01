// Using HashMap
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


// using HashSet
function containsNearbyDuplicate1(nums: number[], k: number): boolean {
  const set = new Set();

  for(let i = 0; i < nums.length; i++) {
    if(set.has(nums[i])) {
      console.log("Number: ", nums[i]);
      return true;
    }

    set.add(nums[i]);

    if(set.size > k) {
      set.delete(nums[i - k]);
    }

    console.log(set, set.size);

  }

  return false;
}

console.log(containsNearbyDuplicate1([1,2,3,4,5,1,2,3,4,5,1,1], 3));
