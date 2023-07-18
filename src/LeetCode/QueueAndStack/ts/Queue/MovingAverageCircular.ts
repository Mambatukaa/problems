import { CircularQueue } from './CircularQueue';

// Space Complexity: O(1)
// Time Complexity: O(n)

class MovingAverageCircular {
  private queue: number[];

  windowSum: number;
  size: number;
  head: number;
  count: number;


  constructor(size: number) {
    this.windowSum = 0;
    this.queue = new Array(size);

    this.size = size;
    this.head = 0;
    this.count = 0;
  }

  next(value: number) {
    ++this.count;

    const tail = (this.head + 1) % this.size;

    const tailNum = this.queue[tail] ?? 0;

    this.windowSum = this.windowSum - tailNum + value;

    this.head = (this.head + 1) % this.size;

    this.queue[this.head] = value;
    

    const result = this.windowSum / Math.min(this.count, this.size);

    console.log(result);

    return result;
  }

}

const movingAverageCircular = new MovingAverageCircular(3);

movingAverageCircular.next(1);
movingAverageCircular.next(2);
movingAverageCircular.next(3);
movingAverageCircular.next(4);
