
// find single one
// XOR operator
// Time Complexity: O(n)
// Space Complexity: O(1)

function singleNumber(nums: number[]): number {
  let answer = 0;

  for(let num of nums) {
    answer ^= num;
  }


  return answer;
}


console.log(singleNumber([2,2,3])); // => 1 
