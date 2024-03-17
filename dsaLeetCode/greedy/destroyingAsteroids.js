/**
 * @param {number} mass
 * @param {number[]} asteroids
 * @return {boolean}
 */

// Time Complexity: O(n)
// Space Complexity: O(1)
var asteroidsDestroyedII = function(mass, asteroids) {
  const minHeap = new MinPriorityQueue();

  for(const asteroid of asteroids) {
    minHeap.enqueue(asteroid);
  };

  while(minHeap.size()) {
    const asteroid = minHeap.dequeue().element;

    if(mass < asteroid) {
      return false;
    };

    mass += asteroid;
  };


  return true;
};

// Time Complexity: O(n log n)
// Space Complexity: O(1)
var asteroidsDestroyed = function(mass, asteroids) {
  asteroids.sort((a, b) => a - b);

  if(asteroids[0] > mass) {
    return false;
  };

  for(const asteroid of asteroids) {
    if(mass < asteroid) {
      return false;
    };

    mass += asteroid;
  }

  return true;
};

