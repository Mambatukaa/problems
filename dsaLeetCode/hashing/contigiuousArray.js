const fn = (nums) => {
  const counts =[0, 0];
  // count zero and nums
  
  for(const num of nums) {
    counts[num]++;
  };

  let leftIdx = 0;
  let rightIdx = nums.length - 1;

  while(leftIdx < rightIdx) {
    // return answer
    if(counts[0] === counts[1]) {
      return rightIdx - leftIdx + 1;
    };

    if(nums[leftIdx] === nums[rightIdx]) {
      counts[nums[rightIdx]]--;
      rightIdx--;

      continue;
    };

    // 0 > 1
    if(counts[0] > counts[1]) {
      nums[leftIdx] === 0 ? leftIdx++ : rightIdx--; 
      counts[0]--;
    } else {
      nums[leftIdx] === 1 ? leftIdx++ : rightIdx--;
      counts[1]--;
    };
  };

  return 0;
}
      //      L                                                                                                                                                                                                     R
const nums = [0,1,0,1,1,1,0,0,1,1,0,1,1,1,1,1,1,0,1,1,0,1,1,0,0,0,1,0,1,0,0,1,0,1,1,1,1,1,1,0,0,0,0,1,0,0,0,1,1,1,0,1,0,0,1,1,1,1,1,0,0,1,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,1,0,1,0,1,1,0,0,1,1,0,1,1,1,1,0,1,1,0,0,0,1,1];
console.log(nums.length)
// 0:3, 1:5
// 

console.log(fn(nums));

/*
        0, 1, 2, 3, 4, 5, 6, 7

nums = [0, 1, 1, 0, 1, 1, 1, 0];

 leftIdx: 0
rightIdx: 7
 leftNum:
rightNum:
  counts:

map = {

};

 */







