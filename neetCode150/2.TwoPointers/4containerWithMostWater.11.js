// OPTIMAL SOLUTION
// TWO POINTERS
// Time Complexity: O(n)
// Space Complexity: O(1)
const maxArea = (height) => {

  const n = height.length;
  let leftIdx = 0;
  let rightIdx = n - 1;

  let res = 0;

  while(leftIdx < rightIdx) {
    const left = height[leftIdx];
    const right = height[rightIdx];

    res = Math.max(res, (rightIdx - leftIdx) * Math.min(right, left));

    if(left > right) {
      rightIdx--;
    } else {
      leftIdx++;
    };

  };

  return res;


};

// brute force
// Time Complexity: O(n^2)
// Space Complexity: O(1)
// TIME LIMIT EXCEEDED
const maxAreaII = (height) => {
  const n = height.length;
  
  let max = 0;
  
  for(let left = 0; left < n; left++) {
    const leftHeight = height[left];
    let min = leftHeight;

    for(let right = left + 1; right < n; right++) {
      const width = right - left;
      const rightHeight = height[right];

      min = Math.min(leftHeight, rightHeight)
      max = Math.max(max, min * width);
    };
  }

  return max;
};

const arr = [1, 8, 6, 2, 5, 4, 8, 3, 7];

console.log(maxArea(arr));
