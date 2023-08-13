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


// if it's already sorted...
// Time Complexity: O(nums1);
// Space Complexity: O(1);
function intersectSorted(nums1: number[], nums2: number[]) {
  if(nums1.length > nums2.length) {
    return intersectSorted(nums2, nums1);
  }

  nums1 = nums1.sort((a, b) => a - b);
  nums2 = nums2.sort((a, b) => a - b);

  console.log("sorted: ", nums1);
  console.log("sorted: ", nums2);

  let p1 = 0;
  let p2 = 0;

  const answer: number[] = [];

  while(p1 < nums1.length) {
    if(nums1[p1] === nums2[p2]) {
      answer.push(nums1[p1])

      p1++;
      p2++;
    } else if(nums1[p1] > nums2[p2]) {
      p2++;
    } else {
      p1++;
    }
  }

  console.log(answer);

  return answer;
}

// intersectSorted([1,2,2,1], [2,2]);
// intersectSorted([4,5,9], [4,4,8,9,9]);

const a = [61,24,20,58,95,53,17,32,45,85,70,20,83,62,35,89,5,95,12,86,58,77,30,64,46,13,5,92,67,40,20,38,31,18,89,85,7,30,67,34,62,35,47,98,3,41,53,26,66,40,54,44,57,46,70,60,4,63,82,42,65,59,17,98,29,72,1,96,82,66,98,6,92,31,43,81,88,60,10,55,66,82,0,79,11,81]
const b = [5,25,4,39,57,49,93,79,7,8,49,89,2,7,73,88,45,15,34,92,84,38,85,34,16,6,99,0,2,36,68,52,73,50,77,44,61,48]


intersectSorted(a, b);

