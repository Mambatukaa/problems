// Time Complexity: O(n)
// Space Complexity: O(1)
const reverseString = (s) => {
  let leftIdx = 0;
  let rightIdx = s.length - 1;

  while(leftIdx < rightIdx) {
    [s[leftIdx], s[rightIdx]] = [s[rightIdx], s[leftIdx]];

    leftIdx++;
    rightIdx--;
  };

  return s;
};

console.log(reverseString(["h", "e", "l", "l", "o"]));
