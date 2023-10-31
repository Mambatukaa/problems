// Time Complexity: O(n)
// Space Complexity: O(n)
const firstDuplicateValueII = (array) => { 
  const set = new Set();

  for(const num of array) {
    if(set.has(num)) {
      return num;
    }

    set.add(num);
  }

  return -1;
}


console.log(firstDuplicateValueII([2,1,4,2,3,3,4]));
