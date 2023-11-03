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

const array = [1,2,3,2,2,1,2];

console.log(majorityElement(array));
