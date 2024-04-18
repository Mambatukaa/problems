
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

/*


timeMap.set("foo", "bar", 1);

if there is actual timestamp return value

  timeMap.get("foo", 1) ====> bar 

if there is not actual timestamp return prev value

  timeMap.get("foo", 3) ====> bar 


one key has multiple values and multiple values can be in multiple timestamp


foo: {
  1: bar,
  2: bar,
  3: bar2,
  4: bar3
  5: bar3
};


get("foo", 10);

1 -> 10

mid = 5;

if(mid exists) {
  go right
} else {
  go left
};

// TIME LIMIT EXCEEDED
  1. Search the previous value from timeStamp.....
    Naive approach check key exists if key exists search using timestamp and decrease and check


  All the timestamp of set are restrictly increasing. Also timestamp is int; 


// 1 to timeStamp


Binary search 
  if midTimeStamp exists
    go right
  else
    go left



  {
    1: bar
    4: bar

    timeStamp = 3;

    [1, 4];
    
    left = 0;
    right = 1;

    midIdx = 0;

    mid = 1;

    if(mid < timeStamp) {
      // go right
    
    } else {
      // go left
    
    }


    1 < 3
      // go right
      left = midIdx + 1; ==> 1 

      left = 1;
      right = 1;

      midIdx = 1;

      mid = 4;


      4 > 3

      left = 1;
      right = 0;

}
}




  }


 
 */






