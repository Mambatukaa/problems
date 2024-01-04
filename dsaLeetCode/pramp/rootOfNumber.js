const fn = (x, n) => {
  let lowerBound = 0;
  let upperBound = Math.max(1, x);

  let approxBound = (lowerBound + upperBound) / 2;

  while(approxBound - lowerBound >= 0.001) {
    console.log(lowerBound, '-', approxBound, '-', upperBound)

    if(Math.pow(approxBound, n) > x) {
      upperBound = approxBound;
    } else if(Math.pow(approxBound, n) < x) {
      lowerBound = approxBound;
    } else {
      break;
    };

    approxBound = (upperBound + lowerBound) / 2;
  };

  return approxBound;
};

const x = 6;
const n = 3;

console.log(fn(x, n));
// 3

