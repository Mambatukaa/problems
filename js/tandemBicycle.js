// Time Complexity: O(nlog * n);
// Space Complexity: O(1);
const tandemBicycle = (redShirtSpeeds, blueShirtSpeeds, fastest) => {
  redShirtSpeeds.sort((a, b) => b - a);
  blueShirtSpeeds.sort((a,b) => fastest ? a - b : b - a);

  console.log(redShirtSpeeds)
  console.log(blueShirtSpeeds)

  const n = blueShirtSpeeds.length;

  let total = 0;

  for(let i = 0; i < n; i++) {
    total += Math.max(blueShirtSpeeds[i], redShirtSpeeds[i]);
  }

  return total;
}

const redShirtSpeeds = [3, 3, 4, 6, 1, 2];
const blueShirtSpeeds = [1, 2, 1, 9, 12, 3];

// false => 25 
// true => 32
// [2,3,5,5,9]
// [1,2,3,6,7]

fastest = true;

console.log(tandemBicycle(redShirtSpeeds, blueShirtSpeeds, false));
