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

// Time Complexity: O(nlog*n)
// Space Complexity: O(1)
const classPhotosII = (blueShirtHeights, redShirtHeights) => {
  blueShirtHeights.sort((a,b) => a - b);
  redShirtHeights.sort((a,b) => a - b);

  let blueBack = true;
  let redBack = true;

  for(let i = 0; i < blueShirtHeights.length; i++) {
    if(blueShirtHeights[i] <= redShirtHeights[i]) {
      blueBack = false;
    }

    if(blueShirtHeights[i] >= redShirtHeights[i]) {
      redBack = false;
    }

  }

  return redBack || blueBack;
}


const blueShirt = [1,2,3];
const redShirt = [2,3,4];


console.log(classPhotosII(blueShirt, redShirt));
