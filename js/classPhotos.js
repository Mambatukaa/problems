// Time Complexity: O(nlog*n)
// Space Complexity: O(1)
const classPhotos = (firstRow, secondRow) => {
  firstRow.sort((a,b) => a - b);
  secondRow.sort((a,b) => a - b);

  // update row
  if(firstRow[0] > secondRow[0]) {
    const temp = firstRow;

    firstRow = secondRow;
    secondRow = temp;
  }

  for(let i = 0; i < firstRow.length; i++) {
    if(firstRow[i] >= secondRow[i]) {
      return false;
    }
  }

  return true;
}

const blueShirt = [1,2,3];
const redShirt = [2,3,4];


console.log(classPhotos(blueShirt, redShirt));
