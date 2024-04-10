
// 8 Minutes
// Time Complexity: O(1)
// Space Complexity: O(1)
var MinStack = function() {
  this.stack = [];
  this.size = 0;
};

/** 
 * @param {number} val
 * @return {void}
 */

// Time Complexity: O(1)
// Space Complexity: O(1)
MinStack.prototype.push = function(val) {
  if(!this.size) {
    this.stack.push([val, val]);
    this.size++;
    return;
  };

  const currMin = this.stack[this.size - 1][0];

  this.stack.push([Math.min(currMin, val), val]);
  this.size++;
};

/**
 * @return {void}
 */

// Time Complexity: O(1)
// Space Complexity: O(1)
MinStack.prototype.pop = function() {
  this.stack.pop();
  this.size--;
};

/**
 * @return {number}
 */
// Time Complexity: O(1)
// Space Complexity: O(1)
MinStack.prototype.top = function() {
  if(!this.size) {
    return null; 
  }

  return this.stack[this.size - 1][1];
};

/**
 * @return {number}
 */
// Time Complexity: O(1)
// Space Complexity: O(1)
MinStack.prototype.getMin = function() {
  if(!this.size) {
    return;
  }

  return this.stack[this.size - 1][0];
    
};

/** 
 * Your MinStack object will be instantiated and called as such:
 * var obj = new MinStack()
 * obj.push(val)
 * obj.pop()
 * var param_3 = obj.top()
 * var param_4 = obj.getMin()
 */
