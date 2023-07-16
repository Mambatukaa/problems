// Time complexity: O(n)
// Space complexity: O(n)
//
class MovingAverageCircular {
  private queue: number[];
  private size: number;
  private windowSum: number;

  constructor(size: number) {
    this.queue = []
    this.size = size;
    this.windowSum = 0;
  }


  next(value: number): number {
    this.queue.push(value);

    const length = this.queue.length;

    this.windowSum = 0;

    let i = Math.max(0, length - this.size);

    console.log("i: ", i);

    for(i; i < length; i++) {
      this.windowSum += this.queue[i]; 
    }


    const result = this.windowSum / Math.min(length, this.size);

    console.log(result);

    return result;
  }

}

const movingAverageCircular = new MovingAverageCircular(3);


movingAverageCircular.next(1)
movingAverageCircular.next(2)
movingAverageCircular.next(3)
movingAverageCircular.next(4)
movingAverageCircular.next(5)
movingAverageCircular.next(6)

