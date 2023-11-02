// Time Complexity: O(n)
// Space Complexity: O(1)
const bestSeat = (seats) => {
  let bestSeat = -1;
  let maxSpace = 0;

  let leftIndex = 0;
  let rightIndex = 1;

  while(rightIndex < seats.length) {
    if(seats[rightIndex] === 0) {
      rightIndex++;
      continue;
    } 

    const newMaxSpace = rightIndex - leftIndex - 1;

    if(maxSpace < newMaxSpace) {
      maxSpace = newMaxSpace;
      bestSeat = Math.floor((leftIndex + rightIndex) / 2);
    }

   leftIndex = rightIndex;
   rightIndex = leftIndex + 1;


  }

  return bestSeat;
}

const seats = [1,1,1,1,1,1];

console.log(bestSeat(seats));
