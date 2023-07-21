function last(arr: any) {
  return arr[arr.length - 1];
}

class MinStack  {
  _stack: number[];
  _minStack: number[][]


  constructor() {
    this._stack = [];
    this._minStack = [];
  }


  push(value: number): void {
    this._stack.push(value);


     if(this._minStack.length === 0 || last(this._minStack)[0] > value ) {
      this._minStack.push([value, 1]);
    } else if(last(this._minStack)[0] === value) {
      last(this._minStack)[1]++;
    }

  }

  pop(): void {

    if(last(this._stack) === last(this._minStack)[0]) {
        last(this._minStack)[1]--;
    }

    if(last(this._minStack)[1] === 0) {
      this._minStack.pop();
    }

    this._stack.pop();
  }

  top(): number {
    return last(this._stack);
  }

  getMin(): number {
    return last(this._minStack)[0];
  }
}

const minStack = new MinStack();

minStack.push(2);
minStack.push(3);
minStack.push(1);
minStack.push(1);
console.log(minStack._minStack);
minStack.pop();
minStack.pop();

console.log(minStack._minStack);
console.log(minStack._stack);
