 // nums = [5, 7, 3, 9, 4, 9, 8, 3, 1]
    // output = 8
    // [3-2, 1-1, 5-1, 9-2, 7 - 1, 8 - 1]
    // 1, 5, 7, 8 unique values ==> 8

    /*
    nums = [9,9,8,8]
    both duplicated
    return : -1;

    1. Map {5: 1, 7: 1, 3: 2, ...}
    2. max num = -1
    3. Iterate through map if(value === 1 && key > maxNu) maxNum

    TC: O(n)
    SC: O(n) ==>

    array = new size(2001);
    num = 5, [0,0,0, 0, 2]

    iterate if(num === 1) {
        max = num
    } 

    return

    TC: O(n)
    SC: O(1) ==> fixed size 2000
    */

 // Time Complexity: O(n)
 // Space Complexity: O(n)
 const fn = (nums) => {
   let maxUniqueNum = -1;
   const map = new Map();

   for(const num of nums) {
       map.set(num, (map.get(num) || 0) + 1);
   };

   for(const [key, value] of map) {
       if(value === 1 && maxUniqueNum < key) {
           maxUniqueNum = key;
       }
   }

   return maxUniqueNum;
 };

 // Time Complexity: O(n)
 // Space Complexity: O(k)
 const fnII = (nums) => {
    const arr = new Array(2001).fill(0);
    let maxNum = -1;

    for(const num of nums) {
        arr[num]++;
    };

    for(let i = 0; i < arr.length; i++) {
        if(arr[i] === 1) {
            maxNum = i;
        }
    };


    return maxNum;
 }

 // Sorting
 // Time Complexity: O(n)
 // Space Complexity: O(k)
 const fnIII = (nums) => {
   nums.sort((a, b) => a - b);

   for(let i = nums.length - 1; i >= 0; i--) {
     if(i === 0 || nums[i - 1] !== nums[i]) {
       return nums[i];
     }

     while(i > 0 && nums[i] === nums[i - 1]) {
       i--;
     }

   };

   return -1;
 };


 const nums = [5, 7, 3, 9, 4, 9, 8, 3, 1];
 console.log(fnIII(nums));
 // 8
