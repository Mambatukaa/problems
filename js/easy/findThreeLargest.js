// Time complexity: O(n)
// Space complexity: O(1)
const findThreeLargets = (arr) => {
  let first = Number.MIN_SAFE_INTEGER;
  let second = Number.MIN_SAFE_INTEGER;
  let third = Number.MIN_SAFE_INTEGER;

  for(let num of arr) {
    if(num > first) {
      third = second;
      second = first;
      first = num;
    } else if(num > second) {
      third = second;
      second = num;
    } else if(num > third) {
      third = num;
    }

  }

  return [third, second, first];
}

const findThreeLargetsII = (arr) => {
  let threeLargest = [null, null, null];

  for(let num of arr) {

    if(threeLargest[2] === null || num > threeLargest[2]) {
      shiftAndUpdate(threeLargest, 2, num);
    } else if(threeLargest[1] === null || num > threeLargest[1]) {
      shiftAndUpdate(threeLargest, 1, num);
    } else if(threeLargest[0] === null || num > threeLargest[0]) {
      shiftAndUpdate(threeLargest, 0, num);
    }

  }

  return threeLargest;
};

const shiftAndUpdate = (arr, idx, num) => {
  for(let i = 0; i < arr.length; i++) {
    if(idx === i) {
      arr[i] = num;
    } else {
      arr[i] = arr[i + 1];
    }
  }

};




console.log(findThreeLargetsII([1,2,3,4,5,6,7]));
