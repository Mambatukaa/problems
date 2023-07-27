function happyNumber(num: number): boolean {
  const seen = new Set();
  let answer = sumOfSquares(num);

  while(!seen.has(answer)) {
    seen.add(answer);
    answer = sumOfSquares(answer);

    if(answer === 1) return true;
  }

  return false;
}

function sumOfSquares(num: number): number {
  let sum = 0;

  while(num > 0) {
    sum += (num % 10) ** 2; 
    num = Math.floor(num / 10);
  }


  return sum;
}

console.log(happyNumber(2));
