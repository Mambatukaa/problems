// Time Complexity: O(nlog(n))
// Space Complexity: O(n)
const sweetAndSavory = (dishes, target) => {
  const sweetDishes = dishes.filter(dish => dish < 0).sort((a,b) => b-a);
  const savoryDishes = dishes.filter(dish => dish > 0).sort((a,b) => a-b);

  let bestPair = [0,0];
  let bestDiff = Infinity;

  let sweetIdx = 0, 
   savoryIdx = 0;

  while(sweetIdx < sweetDishes.length && savoryIdx < savoryDishes.length) {
    const currSum = savoryDishes[savoryIdx] + sweetDishes[sweetIdx];

    if(currSum <= target) {
      const currDiff = target - currSum;

      if(currDiff < bestDiff) {
        bestDiff = currDiff;
        bestPair = [sweetDishes[sweetIdx], savoryDishes[savoryIdx]];
      }

      savoryIdx++;
    } else {
      sweetIdx++;
    }


  }

  return bestPair;

}

const dishes = [-3,-5, 1,7];
const target = 8; // [-1, 7] 6

console.log(sweetAndSavory(dishes, target));

