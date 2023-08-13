// Last in First out data structure
class Stack {
  data: number[];
  private size: number;
  private headIndex: number;

  constructor(size: number) {
    this.size = size;
    this.data = new Array(size);
    this.headIndex = 0;
  }


  push(value: number): void {
    this.isFull();

    this.data[this.headIndex++] = value;

    console.log("Succesffully added to the stack: ", this.data);
  } 

  pop(): void {
    this.isEmpty();

    this.data.splice(-1);

    this.headIndex--;

    console.log("Succesffully removed from the stack: ", this.data, " headIndex: ", this.headIndex);
  }

  top(): number {
    return this.data[this.headIndex];
  }

  isFull(): void {
    if(this.headIndex === this.size) {
      throw new Error('Stack is full')
    }
  }

  isEmpty(): void {
    if(this.headIndex === 0) {
      throw new Error('Stack is empty')
    }
  }
}


const queue = new Stack(5);

queue.push(1);
queue.push(2);
queue.push(3);
queue.push(4);
queue.push(5);


queue.pop();
queue.pop();
queue.pop();
queue.pop();
queue.pop();
queue.pop();

