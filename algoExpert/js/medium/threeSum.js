// Time Complexity: O(n^3);
// Space Complexity: O(n);
const threeSum = (array, targetSum) => {
  const output = [];

  for(let i = 0; i < array.length; i++) {

    for(let j = i + 1; j < array.length; j++) {
      if(i === j) {
        continue;
      }

      for(let k = j + 1; k < array.length; k++) {
        const answer = [];

        if(i === k || j == k) {
          continue;
        }

        if(array[i] + array[j] + array[k] === targetSum) {
          answer.push(array[i], array[j], array[k]);
        }

        if(answer.length) {
          output.push(answer);
        }

      }


    }

  }

  return output

}

// Time Complexity: O(n^2);
// Space Complexity: O(n);
const threeSumII = (array, targetSum) => {
  array.sort((a,b) => a-b);

  const answer = [];

  for(let i = 0; i < array.length - 2; i++) {
    const curr = array[i];

    let leftIndex = i + 1;
    let rightIndex = array.length - 1;

    while(leftIndex < rightIndex) {
      const left = array[leftIndex];
      const right = array[rightIndex];

      const sum = curr + left + right;

      console.log(sum, '-----', targetSum)

      if(sum === targetSum) {
        answer.push([curr, left, right]);

        rightIndex--;
        leftIndex++;
      } else if(sum > targetSum) {
        rightIndex--;
      } else {
        leftIndex++;
      }
    }

  }

  return answer;
}

// Time Complexity: O(n^3);
// Space Complexity: O(n);
const threeSumIII = (array, targetSum) => {
  const map = {};
  const answer = [];

  array.sort((a,b) => a-b);

  for(let i = 0; i < array.length; i++) {
    map[array[i]] = i;
  }

  console.log(map)

  for(const i of array) {
    for(const j of array) {
      if(i === j) continue;

      const targetSumDelta = targetSum - (i + j);

      if(targetSumDelta !== i && targetSumDelta !== j && map[targetSumDelta]) {

        const hit = [i, j, targetSumDelta];
        hit.sort();

        if(searchForArray(answer, hit) === -1)
          answer.push(hit);
      }
    }

  }

  return answer;
}

function searchForArray(haystack, needle){
  var i, j, current;
  for(i = 0; i < haystack.length; ++i){
    if(needle.length === haystack[i].length){
      current = haystack[i];
      for(j = 0; j < needle.length && needle[j] === current[j]; ++j);
      if(j === needle.length)
        return i;
    }
  }
  return -1;
}

const array = [1,2,3,4,0];
const targetSum = 0;

console.log(threeSumIII(array, targetSum));
