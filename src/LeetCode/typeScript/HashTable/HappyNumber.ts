// Time Complexity: O(log n);
// Space Complexity: O(log n);
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


// Time Complexity: O(log n);
// Space Complexity: O(1);
function happyNumberFastSlow(num: number): boolean {
  let slow = num;
  let fast = sumOfSquares(num);

  while(fast !== 1 && slow !== fast) {
    slow = sumOfSquares(slow);
    fast = sumOfSquares(sumOfSquares(fast));

    console.log(slow, ' slow');
    console.log(fast, ' fast fast');
  }

  return fast === 1;
}


console.log(happyNumberFastSlow(19));
