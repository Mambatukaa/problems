


// Solution of some guy/lady
// Time Complexity: O(log n)
// Space Complexity: O(n)
class TimeMap {
  constructor() {
    this.data = new Map();
  }

  set(key, value, timestamp) {
    if(!this.data.has(key)) {
      this.data.set(key, []);
    };

    this.data.get(key).push({timestamp, value})

    console.log(`${value} added in the following ${timestamp} timestamp to the ${key}`)
  };

  get(key, timestamp) {
    if(!this.data.has(key)) {
      return "";
    };

    const values = this.data.get(key); 

    let left = 0;
    let right = values.length - 1;
    let res = ""

    while(left <= right) {
      const mid = Math.floor((left + right) / 2);

      if(values[mid].timestamp === timestamp) {
        // timestamp found
        return values[mid].value;
      };

      if(values[mid].timestamp < timestamp) {
        // go right
        res = values[mid].value;
        left = mid + 1;

      } else {
        // go left
        right = mid - 1;
      };
    };

    return res;
  };

};

const timeMap = new TimeMap();

timeMap.set("foo", "bar", 1);
timeMap.set("foo", "bar2", 4);

console.log(timeMap.data)
console.log(timeMap.get("foo", 5))
