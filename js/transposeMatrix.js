// naive
// Time complexity: O(n * k)
// Space complexity: O(n * k)
const transposeMatrix = (matrix) => {
  const answer = [];

  for(arr of matrix) {
    for(let i = 0; i < arr.length; i++) {
      if(!answer[i]) {
        answer[i] = [];
      }

      answer[i].push(arr[i]);
    }
  }


  return answer; 
}


// Time complexity: O(n * k)
// Space complexity: O(n * k)
const transposeMatrixII = (matrix) => {
  const answer = [];

  for(let col = 0; col < matrix[0].length; col++) {

    const newRow = [];

    for(let row = 0; row < matrix.length; row++) {
      newRow.push(matrix[row][col]);
    }

    answer.push(newRow);
  }

  return answer; 
}


const matrix = [[1,2], 
                [3,4], 
                [5,6]
               ];

console.log(transposeMatrixII(matrix));
