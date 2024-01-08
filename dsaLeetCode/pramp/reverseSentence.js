// Time Complexity: traversing the array twice with a constant number of actions for each item is linear O(N).
// Space Complexity: using iteration indices and one temp variable takes constant O(1) memory.
const fn = (arr) => {
  const n = arr.length;

  mirrorReverse(arr, 0, n - 1);

  let l = null;

  for(let r = 0; r < n; r++) {
    // reach the first sentence
    if(arr[r] === " ") {
      if(l !== null) {
        mirrorReverse(arr, l, r - 1);
        l = null;
      }
    } else if(r >= n - 1) {
      // reach the end
      if(l !== null) {
        mirrorReverse(arr, l, r);
      }
    } else if(l === null) {
       l = r;
    } 
  };

  return arr;
};

const mirrorReverse = (arr, l, r) => {
  while(l < r) {
    [arr[l], arr[r]] = [arr[r], arr[l]];

    l++;
    r--;
  };
};

// const arr = ['w', 'o', 'r', 'l', 'd', ' ', 'h', 'e', 'l', 'l', 'o'];
const arr = ["a"," ", " ", "b"];
// l
//     r
// "bxxa"

console.log(fn(arr));
