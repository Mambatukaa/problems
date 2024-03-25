
// Time Complexity: O(n log n)
// Space Complexity: O(n)
var findLeastNumOfUniqueInts = function(arr, k) {

  const map = new Map();

  for(const num of arr) {
    map.set(num, (map.get(num) || 0) + 1);
  };

  let ordered = [];

  for(const val of map.values()) {
    ordered.push(val);
  };

  ordered.sort((a, b) => b - a);

  while(k > 0) {
    let val = ordered[ordered.length - 1];

    if(val <= k) {
      k -= val;
      ordered.pop();
    } else {
      break;
    };

  };

  return ordered.length;
};

// Time Complexity: O(n log n)
// Space Complexity: O(n)
var findLeastNumOfUniqueIntsII = function(arr, k) {
  const map = new Map();

  for(const num of arr) {
    map.set(num, (map.get(num) || 0) + 1);
  };

  const sortedMap = new Map([...map.entries()].sort((a, b) => a[1] - b[1]));

  while(k > 0) {
    const key = sortedMap.keys().next().value;

    sortedMap.set(key, sortedMap.get(key) - 1);

    if(sortedMap.get(key) === 0) {
      sortedMap.delete(key);
    };

    k--;
  };

  return sortedMap.size;
};

const arr = [5, 5, 4];
const k = 1;

console.log(findLeastNumOfUniqueInts(arr, k));
