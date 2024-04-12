
/**
 * @param {number} target
 * @param {number[]} position
 * @param {number[]} speed
 * @return {number}
 */
 // Time Complexity: O(n log n)
 // Space Complexity: O(n)
 // Gave up
var carFleet = function(target, position, speed) {
  const pairs = [];
  let n = position.length;

  for(let i = 0; i < n; i++) {
    const pos = position[i];
    const spe = speed[i];

    pairs.push([pos, spe]);
  };

  // sort by position
  pairs.sort((a, b) => a[0] - b[0]);

  console.log(pairs)

  while(pairs.length > 1) {
    const first = pairs.pop();
    const second = pairs.pop();

    const firstCarTime = (target - first[0]) / first[1];
    const secondCarTime = (target - second[0]) / second[1]; 

    // first car can pass the second car 
    // then merge
    if(firstCarTime >= secondTime) {
      pairs.push(first);
      n--;
    } else {
      pairs.push(second);
    };
  };

  return n;
};



/*

MAKE a pair using position and speed

target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3];

pairs = [[10, 8], [8, 4], [0, 1], [5, 1], [3, 3]]

SORT pairs BY POSITION

pairs = [[0, 1], [3, 3], [5, 1], [8, 4], [10, 8]];


Check the last 2nd car can pass the the last car or not.
  If the car can pass it this means they become one fleet
    Merge the cars (Remove the car which has higher speed)
  If cannot pass it the last car will be one fleet
    Remove last car and increase the fleets because no car can pass it
  
  To check car can pass or not. COMPARE( FIRST(target - position) / speed, SECOND(target - position) / Speed)

  totalTimeToReachTarget = (target - position) / speed;





*/
