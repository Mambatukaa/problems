/**
 * @param {number} k
 * @param {number[]} nums
 */
// Time Complexity: O(n * log k)
// Space Complexity: O(n)
var KthLargest = function(k, nums) {
  this.k = k;
  this.minHeap = new MinPriorityQueue();

  this.addVal = (num) => {
    this.minHeap.enqueue(num);

    if(this.minHeap.size() > k) {
      this.minHeap.dequeue();
    }
  };

  for(const num of nums) {
    this.addVal(num);
  };

};

/** 
 * @param {number} val
 * @return {number}
 */
KthLargest.prototype.add = function(val) {
  this.addVal(val);
  return this.minHeap.front().element;
};

/** 
 * Your KthLargest object will be instantiated and called as such:
 * var obj = new KthLargest(k, nums)
 * var param_1 = obj.add(val)
 */

/**
 * @param {number} k
 * @param {number[]} nums
 */

// Time Complexity: O(n * log n)
// Space Complexity: O(n)
var KthLargestII = function(k, nums) {
  this.k = k;
  this.nums = nums;
};

/** 
 * @param {number} val
 * @return {number}
 */
KthLargestII.prototype.add = function(val) {
  this.nums.push(val);

  this.nums.sort((a, b) => b - a);

  return this.nums[k];
};

/** 
 * Your KthLargest object will be instantiated and called as such:
 * var obj = new KthLargest(k, nums)
 * var param_1 = obj.add(val)
 */
