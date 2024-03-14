var MedianFinder = function() {
  this.minHeap = new MinPriorityQueue();
  this.maxHeap = new MaxPriorityQueue();
};

/** 
 * @param {number} num
 * @return {void}
 */
 // Time Complexity: O(log n) 
 // Space Complexity: O(n) 
MedianFinder.prototype.addNum = function(num) {
  // MIN heap but elements must be less or equal than MIN heap elements
  // add elements to the max queue
  this.maxHeap.enqueue(num);
  
  // add maxHeap's max element to the min heap
  this.minHeap.enqueue(this.maxHeap.dequeue().element);

  if(this.minHeap.size() > this.maxHeap.size()) {
    // add min element to the maxHeap
    this.maxHeap.enqueue(this.minHeap.dequeue().element)
  };
};

/**
 * @return {number}
 */
MedianFinder.prototype.findMedian = function() {
  // MAX heap has must be more element than MIN heap
  const maxSize = this.maxHeap.size()
  const minSize = this.minHeap.size();

  if(maxSize > minSize ) {
    return this.maxHeap.front().element;
  };

  return (this.minHeap.front().element + this.maxHeap.front().element) / 2;
};

/** 
 * Your MedianFinder object will be instantiated and called as such:
 * var obj = new MedianFinder()
 * obj.addNum(num)
 * var param_2 = obj.findMedian()
 */


 // declare two heaps (max, min)
 // 
 // add num and find median
 //

 /*


var MedianFinder = function() {
  this.data = [];
};

/** 
 * @param {number} num
 * @return {void}
 */
 /*
MedianFinder.prototype.addNum = function(num) {
  console.log(this.data, '===============');
  if(!this.data.length) {
    this.data.push(num)
  } else {
    for(let i = 0; i < this.data.length; i++) {
      const curr = this.data[i];
      if(curr > num) {
        this.data.splice(i, 0, num);
        return;
      };
    }

    this.data.push(num);
  };
    
};

/**
 * @return {number}
 */
 /*
MedianFinder.prototype.findMedian = function() {
  // even
  const idx = Math.floor(this.data.length / 2);

  if(this.data.length % 2 === 0) {
    return (this.data[idx] + this.data[idx-1]) / 2;
  };

  return this.data[idx];
};
*/

/** 
 * Your MedianFinder object will be instantiated and called as such:
 * var obj = new MedianFinder()
 * obj.addNum(num)
 * var param_2 = obj.findMedian()
 */


