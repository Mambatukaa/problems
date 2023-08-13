// Time complexity: O(n)
// Space complexity: O(n)
//
class MovingAverageArray {
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

const movingAverageArray = new MovingAverageArray(3);


movingAverageArray.next(1)
movingAverageArray.next(2)
movingAverageArray.next(3)
movingAverageArray.next(4)
movingAverageArray.next(5)
movingAverageArray.next(6)

