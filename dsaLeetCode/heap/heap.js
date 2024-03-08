// heap implementation

class Heap {
  // min heap parent <= children
  // max heap parent > children
 
  constructor(heapSize, heapType) {
    this.heap = new Array(heapSize + 1).fill(-1);
    this.sizeOfTree = 0;
    this.heapType = heapType;
  };

  insert(value) {
    this.sizeOfTree++;
    this.heap[this.sizeOfTree] = value;

    this.heapifyBottomToTop(this.sizeOfTree);

  };

  isEmpty() {
    return this.sizeOfTree === 0;
  };

  peek() {
    if(this.isEmpty) {
      console.log("Head is empty");
      return
    }

    return this.heap[1];
  }

  sizeOfBP() {
    return this.sizeOfTree;
  };

  levelOrder() {
    for(let i = 1; i <= this.sizeOfTree; i++) {
      console.log(this.heap[i]);
    }

  };

  // heapify for Insert
  // Time Complexity: O(log n)
  // Space Complexity: O(log n)
  heapifyBottomToTop(index) {
    if(index <= 1) {
      return;
    };

    const parentIdx = Math.floor(index / 2);
    const parentVal = this.heap[parentIdx];
    const currentVal = this.heap[index];

    if(this.heapType === 'min') {

      if(parentVal > currentVal) {
        // switch
        [this.heap[parentIdx], this.heap[index]] = [this.heap[index], this.heap[parentIdx]];
      };

    } else {
      // max heap
      
      if(parentVal < currentVal) {
        // switch
        [this.heap[parentIdx], this.heap[index]] = [this.heap[index], this.heap[parentIdx]];

        this.heapifyBottomToTop(parentIdx)
      };

    };

    this.heapifyBottomToTop(parentIdx) // O(log n)
  };


  heapifyTopToBottom(index = 1) {
    const leftChildIdx = index * 2;
    const rightChildIdx = index * 2 + 1;
    let swapChild;

    if(this.sizeOfTree < leftChildIdx) {
      return;
    };

    if(this.heapType === "max") {
      // only one child
      if(this.sizeOfTree === leftChildIdx) {

        if(this.heap[index] < this.heap[leftChildIdx]) {
          [this.heap[index], this.heap[leftChildIdx]] = [this.heap[leftChildIdx], this.heap[index]];
        };

        return;
      } else {
        // two children
        if(this.heap[leftChildIdx] > this.heap[rightChildIdx]) {
          swapChild = leftChildIdx;
        } else {
          swapChild = rightChildIdx;
        };

        // swap
        if(this.heap[swapChild] > this.heap[index]) {
          [this.heap[index], this.heap[swapChild]] = [this.heap[swapChild], this.heap[index]];
        };

      };


    } else {
      // min heap
      // one child
      if(leftChildIdx === this.sizeOfTree) {
        if(this.heap[leftChildIdx] < this.heap[index]) {
          // swap
          [this.heap[leftChildIdx], [this.heap[index]]] = [this.heap[index], this.heap[leftChildIdx]];
        };

        return;
      } else {
        // two children
        if(this.heap[leftChildIdx] < this.heap[rightChildIdx]) {
          swapChild = leftChildIdx;
        } else {
          swapChild = rightChildIdx;
        };

        // swap
        if(this.heap[swapChild] < this.heap[index]) {
          [this.heap[index], this.heap[swapChild]] = [this.heap[swapChild], this.heap[index]]
        }
      }
    };

    this.heapifyTopToBottom(swapChild);
  };

  // only extract root node
  extract() {
    if(this.isEmpty()) {
      console.log("Heap is empty.")
      return;
    };

    [this.heap[1], this.heap[this.sizeOfTree]] = [this.heap[this.sizeOfTree], this.heap[1]];

    this.heap[this.sizeOfTree] = -1;
    this.sizeOfTree--;

    this.heapifyTopToBottom();
  };

  deleteHeap() {
    this.heap = null;
  };

  // heapify max
  heapify(arr, index) {
    // [-1, 50, 10, 30, 70, 20, 40]

    const n = arr.length;
    const leftChildIdx = index * 2 + 1;
    const rightChildIdx = index * 2 + 2;
    let largestIdx = index;

    if(leftChildIdx < n && arr[leftChildIdx] > arr[largestIdx]) {
      largestIdx = leftChildIdx;
    };

    if(rightChildIdx < n && arr[rightChildIdx] > arr[largestIdx]) {
      largestIdx = rightChildIdx;
    };

    if(index !== largestIdx) {
      //swap
      [arr[index], arr[largestIdx]] = [arr[largestIdx], arr[index]];
      
      this.heapify(arr, largestIdx);
    };
  };

};


// heap size
const h = new Heap(8, 'min');

const array = [50, 10, 30, 70, 20, 40]

console.log(array, 'before')

for(let i = Math.floor(array.length / 2) - 1; i >= 0; i--) {
  h.heapify(array, i)
}

console.log(array, 'after')

/*

0: x
1: 5
2: 10
3: 20
4: 30
5: 40
6: 50
7: 60
8: 



*/
