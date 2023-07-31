// Time Complexity: O(n1 + n2);
// Space Complexity: O(1)
function intersect(nums1: number[], nums2: number[]): number[] {
  const map = new Map();
  const answer: number[] = [];

  for(let i = 0; i < nums1.length; i++) {

    if(map.has(nums1[i])) {
      map.set(nums1[i], map.get(nums1[i]) + 1);

      continue;
    }

    map.set(nums1[i], 1); 
  }


  for(let i = 0; i < nums2.length; i++) {
    if(map.has(nums2[i]) && map.get(nums2[i]) > 0) {
      answer.push(nums2[i]);

      map.set(nums2[i], map.get(nums2[i]) - 1)
    }
  }

  console.log(answer);


  return answer;
}

intersect([4,9,5], [9,4,9,8,4]);
