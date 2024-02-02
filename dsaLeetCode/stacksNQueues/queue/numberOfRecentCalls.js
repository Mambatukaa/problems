// Space Complexity: O(1)
var RecentCounter = function() {
    this.queue = [];
};

/** 
 * @param {number} t
 * @return {number}
 */
// Time Complexity: O(n)
// Space Complexity: O(1)
RecentCounter.prototype.ping = function(t) {
  this.queue.push(t);

  while(this.queue[0] < t - 3000) {
    this.queue.shift();
  }; 

  return this.queue.length;
};

/** 
 * Your RecentCounter object will be instantiated and called as such:
 * var obj = new RecentCounter()
 * var param_1 = obj.ping(t)
 */


 /*
  [1, 100, 3001, 3002]


  newRequest
  oldRequest = queue[0];


  while(oldRequest < newRequest - 3000) {
    oldRequest = queue.shift();
  }

  return queue.length;


 */
