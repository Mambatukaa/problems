/**
 * @param {number[]} dist
 * @param {number} hour
 * @return {number}
 */
// Time Complexity: O(n * log k)
// Space Complexity: O(1)
var minSpeedOnTime = function(dist, hour) {
  if(dist.length - 1 >= hour) {
    return -1;
  };

  const check = (mid) => {

    // check is it possible to reach the office in mid hour
    let totalHour = 0;

    for(let i = 0; i < dist.length - 1; i++) {
      totalHour += Math.ceil(dist[i] / mid);
    };

    totalHour += dist[dist.length - 1] / mid;

    console.log(mid, totalHour)

    return totalHour <= hour;
  };

  let left = 1;
  let right = Math.pow(10, 9)

  while(left <= right) {
    const mid = Math.floor((left + right) / 2);

    if(check(mid)) {
      // decrease
      right = mid - 1;
    } else {
      // decrease
      left = mid + 1;
    };
  };

  return left;
};

const dist = [1,1];

const hour = 1.0;

console.log(minSpeedOnTime(dist, hour), '=========');


/*

dist = [1, 3, 2]; hour = 6;

return min integer speed (in kilometers per hour); if I can't reach the office on giving hour return -1;


EXAMPLE 1:
6 hours limit;

train 1 takes 1 hour
train 2 takes 3 hour
train 3 takes 2 hour

base case

if(dist.length - 1 > hour) {
  return -1;
};


BINARY SEARCH

left = 1;
right = Math.max(...dist);

Check if it's possible to reach the office with mid speed.
  if it's true
    decrease and try
  else
    increase and try

the left must be the actual hour to reach the office;

the last train can be float number




*/
