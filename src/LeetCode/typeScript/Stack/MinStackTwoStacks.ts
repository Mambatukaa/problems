function last(arr: number[]) {
  return arr[arr.length - 1];
}

class MinStack {
  _stack: number[];
  _minStack: number[];

  constructor() {
    this._stack = [];
    this._minStack = [];
  }

  push(value: number): void {
    this._stack.push(value);

    if(this._minStack.length === 0 || last(this._minStack) >= value) {
      this._minStack.push(value);
    }

  }

  pop(): void {

    if(last(this._minStack) == last(this._stack)) {
      this._minStack.pop();
    }

    this._stack.pop();

  }

  top(): number {
    return last(this._stack);
  }

  getMin(): number {
    return last(this._minStack);
  }

}

const minStack = new MinStack();

minStack.push(1);
minStack.push(2);
minStack.push(3);
minStack.push(4);
minStack.push(5);
minStack.push(-1);


console.log(minStack._stack);
console.log(minStack._minStack);
console.log(minStack.getMin());
