class Logger {
  map: any;  

  constructor() {
    this.map = new Map();
  }

  shouldPrintMessage(timestamp: number, message: string): boolean {
    if(!this.map.has(message) || this.map.get(message) <= timestamp) {
      this.map.set(message, timestamp + 10);

      return true;
    }

    return false;
  }

}

const logger = new Logger();

console.log(logger.shouldPrintMessage(1, "foo"));  // return true, next allowed timestamp for "foo" is 1 + 10 = 11
console.log(logger.shouldPrintMessage(2, "bar"));  // return true, next allowed timestamp for "bar" is 2 + 10 = 12
console.log(logger.shouldPrintMessage(3, "foo"));  // 3 < 11, return false
console.log(logger.shouldPrintMessage(8, "bar"));  // 8 < 12, return false
console.log(logger.shouldPrintMessage(10, "foo")); // 10 < 11, return false
console.log(logger.shouldPrintMessage(11, "foo")); // 11 >= 11, return true, next allowed timestamp for "foo" is 11 + 10 = 21


console.log('---------------------------------------');

console.log(logger.shouldPrintMessage(1, "ball"));
console.log(logger.shouldPrintMessage(11, "ball"));
console.log(logger.shouldPrintMessage(21, "ball"));

console.log(logger.map);
