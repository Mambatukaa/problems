//
// max number which has max digits
// Time Complexity: O(n)
// Space Complexity: O(1)
const getMaxLuckyNumber = (x, y, n) => {
  if(x > y) {
    return getMaxLuckyNumber(y, x, n);
  };

  // x = min;
  // y = max;
  
  // try to create max lucky number only using min value

  // we need to mix numbers to create max lucky number
  // we can create max number to using the min element mostly
  
  let totalMinValue = Math.floor(n / x);
  let totalMaxValue = 0;
  let remainder = n % x;

  while(totalMinValue * x + totalMaxValue * y !== n) {

    // try to create remainder using max element
    if(remainder % y === 0) {
      totalMaxValue = remainder / y;
      break;
    };

    totalMinValue -= 1;
    remainder += x;
  };

  return y.toString().repeat(totalMaxValue) + x.toString().repeat(totalMinValue);
};

console.log(getMaxLuckyNumber(4, 8, 20))

// try to create remainder using max value
  // if it's impossible
    // decrease min value and try again
  // once we reach the n this must be the answer;
/*
 

   EXAMPLE 1:
   
   x = 3;
   y = 4;
   sum = 13;

  LUCKY NUMBERS:
     3334
     3343
     3433
     4333


  ANSWER: 4333

**********************************************************************

  EXAMPLE 2:

  x = 7
  y = 5
  n = 22;


  Lucky Numbers:
    
    5557
    5575
    5755
    7555

  ANSWER: 4333

**********************************************************************

  EXAMPLE 3:

  x = 4;
  y = 8
  n = 20;

  884
  848
  488
  4448
  4484
  4844
  8444
  44444

  Answer: 44444



  1. If we can build numbers only using small numbers this will be the biggest number;

    else starts with biggest number will be the highest one

  2. Try to create biggest number using only small value
      if(n % x === 0)
        // we can create the number only using small values

  3. If it's 


 */
