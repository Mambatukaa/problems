/**
 * @param {number} size
 */
// Space Complexity: O(size)
// Time Complexity: O(1)
var MovingAverage = function(size) {
  this.queue = [];
  this.size = size;
  this.curr = 0;
};

/** 
 * @param {number} val
 * @return {number}
 */
// Space Complexity: O(1)
// Time Complexity: O(size) size is constant
MovingAverage.prototype.next = function(val) {
  this.queue.push(val);
  this.curr += val;

  while(this.queue.length > this.size) {
    this.curr -= this.queue.shift();
  };


  return this.curr / this.queue.length;
    
};

/** 
 * Your MovingAverage object will be instantiated and called as such:
 * var obj = new MovingAverage(size)
 * var param_1 = obj.next(val)
 */


 /*
 queue = [3];

  1 => 10 => 3 => 5
  1 => 5.5 => 4.6 => 6

  while(this.queue.length > this.size) {
    curr -= this.queue.shift();
  };

  this.curr += val;

  return this.curr / this.queue.length;

 */
