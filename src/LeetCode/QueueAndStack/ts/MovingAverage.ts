import { CircularQueue } from './CircularQueue';

class MovingAverage {
  private size: number;
  private count: number;
  private windowSum: number;

  queue: any;

  constructor(size: number) {
    this.size = size;
    this.queue = new CircularQueue(size);
    this.count = 0;
    this.windowSum = 0;
  }

  next(value: number): number {
    const isLimitReached = this.count == this.size;

    this.count = isLimitReached ? this.size : ++this.count;

    const firstElement = isLimitReached ? this.queue.poll() : 0;

    this.queue.enqueue(value);
    this.windowSum = this.windowSum - firstElement + value;


    return this.windowSum / this.count

    
  }

}


const movingAverage = new MovingAverage(5);

console.log(movingAverage.next(1));
console.log(movingAverage.next(2));
console.log(movingAverage.next(3));
console.log(movingAverage.next(4));
console.log(movingAverage.next(5));


// [1,2,3,4,5];
// size == 2
// 1 ==> 1 ==> 1
// 2 ==> 1 + 2 ==> 1.5
// 3 ==> 2 + 3 ==> 2.5


// moving window
// 1. create queue
// 2. add queue until size
