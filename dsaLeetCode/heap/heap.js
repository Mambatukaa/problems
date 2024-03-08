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

  levelOrder() {
    for(let i = 1; i < this.sizeOfTree; i++) {
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

};


// heap size
const h = new Heap(8, 'max');

h.insert(20)
h.insert(10)
h.insert(5)
h.insert(60)
h.insert(50)
h.insert(40)
h.insert(30)

h.levelOrder()

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
