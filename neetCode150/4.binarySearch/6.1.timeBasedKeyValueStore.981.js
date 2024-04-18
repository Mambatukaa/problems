
// Time Complexity: O(log n)
// Space Complexity: O(n)
// 1 hour
var TimeMap = function() {
  this.timestamps = new Map();
  this.data = new Map();
};

/** 
 * @param {string} key 
 * @param {string} value 
 * @param {number} timestamp
 * @return {void}
 */
TimeMap.prototype.set = function(key, value, timestamp) {
  if(!this.data.has(key)) {
    this.data.set(key, new Map());
    this.timestamps.set(key, []);
  };

  this.data.get(key).set(timestamp, value);
  this.timestamps.get(key).push(timestamp);
};

/** 
 * @param {string} key 
 * @param {number} timestamp
 * @return {string}
 */
TimeMap.prototype.get = function(key, timestamp) {
      if(!this.data.has(key)) {
      return "";
    };

    const value = this.data.get(key); 

    if(value.has(timestamp)) {
      return value.get(timestamp);
    };

    const timestamps = this.timestamps.get(key);

    let left = 0;
    let right = timestamps.length - 1;

    while(left <= right) {
      const mid = Math.floor((left + right) / 2);

      if(timestamps[mid] > timestamp) {
        // go left
        right = mid - 1;

      } else {
        // go right
        left = mid + 1;
      }

    };


    return value.get(timestamps[right]) ? value.get(timestamps[right]) : "";



};

/** 
 * Your TimeMap object will be instantiated and called as such:
 * var obj = new TimeMap()
 * obj.set(key,value,timestamp)
 * var param_2 = obj.get(key,timestamp)
 */


