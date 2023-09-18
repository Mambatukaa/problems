// Space Complexity: O(n)
// Time Complexity: O(n)
const sortedSquaredArray = (array) => {
  let idx = right = array.length - 1;
  let left = 0;

  const answer = new Array(idx);

  while(left <= right) {
    const leftVal = Math.abs(array[left]);
    const rightVal = Math.abs(array[right]);

    if(leftVal <= rightVal) {
      answer[idx] = rightVal * rightVal;
      right--;
    } else {
      answer[idx] = leftVal * leftVal;
      left++;
    }

    idx--;
  }


  return answer;
}

// Space Complexity: O(n) // new output array
// Time Complexity: O(n * logn)
const sortedSquaredArrayII = (array) => {
  return array.map(el => el * el).sort((a,b) => a-b);
}



console.log(sortedSquaredArray([-4,-3,1,2,5]));
