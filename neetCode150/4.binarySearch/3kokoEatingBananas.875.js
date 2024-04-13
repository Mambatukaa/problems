/**
 * @param {number[]} piles
 * @param {number} h
 * @return {number}
 */
// GREEDY
// Time Complexity: O(log (max(p)) * p)
// Space Complexity: O(1)
// THE REASON WHY LOWER STARTS FROM 1 is if piles has 1 element the choosing min won't work
// Gave up
var minEatingSpeed = function(piles, h) {
  let left = 1;
  let right = Math.max(...piles);

  const calculate = (bananasPerHour) => {
    let hours = 0;
  
    for(let i = 0; i < piles.length; i++) {
      hours += Math.ceil(piles[i] / bananasPerHour);

    };

    return hours;
  };

  while(left <= right) {
    const bananas = Math.floor((left + right) / 2);

    // check how many hours Koko spend to eat mid bananas
    const hoursToFinish = calculate(bananas);

    if(hoursToFinish <= h) {
      right = bananas - 1
    } else {
      left = bananas + 1;
    }

  };

  return left; 
};

const piles = [30, 11, 23, 4, 20];
const h = 8;

console.log(minEatingSpeed(piles, h));



/*

Binary search 1 to max(...piles)

left = 1
right = Max(...piles)


Ability to eat in MID hours
  If can
    Try to eat min bananas
  Else
    Try to eat more bananas
  

The answer will be left + 1;





 */
