const reverseString = (string) => {
  const arr = string.split("");

  let l = 0;
  let r = string.length - 1;

  while(l < r) {
    [arr[l], arr[r]] = [arr[r], arr[l]];

    l++;
    r--;
  };

  return arr.join("");
};

// Time Complexity: O(n);
// Space Complexity: O(1);
const fn = (s) => {
  const arr = s.split(" ");

  for(let i = 0; i < arr.length; i++) {
    arr[i] = reverseString(arr[i]);
  }

  return arr.join(" ");
};

const s = "Let's take LeetCode contest";

console.log(fn(s));
