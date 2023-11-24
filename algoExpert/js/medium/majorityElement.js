// You can assume that the input array will always have a majority element
// Time complexity: O(n^2)
// Space complexity: O(1)
const majorityElement = (array) => {
  let mostCommonItem = [0,0];

  for(let i = 0; i < array.length; i++) {
    let total = 1;
    const current = array[i];

    for(let j = i + 1; j < array.length; j++) {
      if(array[i] === array[j]) {
        total++;
      }
    }

    if(mostCommonItem[1] < total) {
      mostCommonItem = [current, total];
    }
  }

  const [item, count] = mostCommonItem;

  return array.length / 2 < count ? item : -1;
}

const majorityElementII = (array) => {
  let count = 0;
  let answer = null;

  for(const num of array) {
    if(count === 0) answer = num;

    if(num === answer) {
      count++;
    } else {
      count--;
    }
  }

  console.log(answer);

  return answer;
}

const array = [1,2,3,2,2,1,2];

console.log(majorityElementII(array));
