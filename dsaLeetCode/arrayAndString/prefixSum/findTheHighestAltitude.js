// Space Complexity: O(1)
// Time Complexity: O(n)
const fn = (gain) => {
  let max = 0;
  let total = 0;


  for(const altitude of gain) {
    total += altitude;

    max = Math.max(total, max);
  };

  return max;
};


const gain = [-5, 1, 5, 0, -7];

console.log(fn(gain));
