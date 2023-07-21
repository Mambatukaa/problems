function last(array: any[]): any[] {
  return array[array.length - 1];

}

// Time Complexity: O(1)
// Space Complexity: O(n)
class MinStack {
  _stack: any[];

  constructor() {
    this._stack = [];
  }

  push(value: number): void {
    if(this._stack.length === 0) {
      this._stack.push([value, value]);

      return;
    }

    const currentMin = Math.min(value, last(this._stack)[1]);

    this._stack.push([value, currentMin]);
  }

  pop(): void {
    this.isEmpty();

    this._stack.pop();
  }

  top(): number {
    this.isEmpty();

    return last(this._stack)[0];
  }

  getMin(): number {
    return last(this._stack)[1];
  }

  isEmpty(): void {
    if(this._stack.length === 0) {
      throw new Error("The Stack is empty!")
    }
  }
}


const minStack = new MinStack();
minStack.push(1);
minStack.push(2);
minStack.push(3);
minStack.push(4);
minStack.push(5);
minStack.push(-1);
minStack.push(-2);

console.log(minStack.top());
console.log(minStack.top());

console.log(minStack._stack);

