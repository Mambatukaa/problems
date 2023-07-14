class CircularQueue<T> {
  private storage: number[] = [];
  private size: number;

  private headIndex: number;
  private tailIndex: number;

  // constructor function
  constructor(size: number) {
    console.log(`The queue which has ${size} elements created.`);

    this.storage = new Array<number>(size);
    this.size = size;

    this.headIndex = -1;
    this.tailIndex = -1;
  }

  // add an element into the storage
  enqueue(item: number): boolean {
    if(this.isFull()) {
      throw new Error('The queue is full');
    }

    if(this.isEmpty()) {
      this.headIndex = 0;
    }

    this.tailIndex = (this.tailIndex + 1) % this.size;
    this.storage[this.tailIndex] = item; 

    return true;
  }


  // remove an element from the storage
  dequeue(): boolean {
    if(this.isEmpty()) {
      throw new Error("The queue is empty!");
    }

    if(this.headIndex === this.tailIndex) {
      this.headIndex = -1;
      this.tailIndex = -1;

      return true;
    }

    this.headIndex = (this.headIndex + 1) % this.size;

    return true;
  }


  // check the storage is empty
  isEmpty() {
    return this.headIndex === -1;
  }

  // check the storage is full
  isFull() {
    return (this.tailIndex + 1) % this.size === this.headIndex;
  }

  // traversal
  traversal(): void {
    let i = this.headIndex;

    while(i != this.tailIndex) {
      console.log(this.storage[i] + " => ");

      i = (i + 1) % this.size;
    }

    // print the last element of the queue
    console.log(this.storage[this.tailIndex]);
  }


  // return first element
  front(): number {
    if(this.isEmpty()) {
      return -1;
    }

    return this.storage[this.headIndex];
  }

  // return last element
  rear(): number {
    if(this.isEmpty()) {
      return -1;
    }

    return this.storage[this.tailIndex];
  }

}


const queue = new CircularQueue(5);

console.log("is empty ",  queue.isEmpty());
console.log("is full ", queue.isFull());



queue.enqueue(1);
queue.enqueue(2);
queue.enqueue(3);
queue.enqueue(4);
queue.enqueue(5);
queue.traversal();

queue.dequeue();
queue.enqueue(6);


console.log(queue.rear(), " last element");
console.log(queue.front(), " first element");

