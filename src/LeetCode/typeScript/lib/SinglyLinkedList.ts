class MyNode {
  public value: number | null;
  public next: any;

  constructor(value: number | null = null) {
    this.value = value;
    this.next = null
  }

  print(): void {
    console.log("Value: ", this.value, " Next: ", this.next);
  }

}

class LinkedList {
  public head: MyNode
  public size: number;

  constructor() {
    this.head = new MyNode();
    this.size = 0;
  }


  get(index: number): number {
    if(this.head === null || index >= this.size) {
      return -1;
    }

    let tempNode: any = this.head;

    for(let i = 0; i < index; i++) {
      tempNode = tempNode.next;
    }

    return tempNode.value;
  }

  addAtIndex(index: number, value: number): void {
    if(index > this.size) {
      console.log("Index must be less than the size.")
      return;
    }

    if(index < 0) {
      index = 0;
    }

    if(!this.head.value) {
      this.head.value = value;

      this.size++;

      return;
    }

    const newNode = new MyNode(value);

    if(index === 0) {
      newNode.next = this.head;
      this.head = newNode;
    } else {
      let pred = this.head;

      for(let i = 0; i < index - 1; i++) {
        pred = pred.next;
      }

      newNode.next = pred.next;
      pred.next = newNode;
    }

    this.size++;
  }


  removeAtIndex(index: number): void {
    if(this.head === null) {
      console.log("Linked list is empty!");
      return;
    }

    if(index >= this.size) {
      console.log("The index must be less than the size.")
      return;
    }

    this.size--;

    if(index === 0) {
      this.head = this.head.next;
    } else {

      let pred = this.head;

      for(let i = 0; i < index - 1; i++) {
        pred = pred.next;
      }

      pred.next = pred.next.next;
    }
  }

  search(value: number): number {
    if(this.head === null) {
      console.log("LinkedList is empty!")
      
      return - 1;
    }

    let pred = this.head;

    for(let i = 0; i < this.size; i++) {
      if(pred.value === value) {
        console.log("The value found at index of: ", i);

        return pred.value;
      }

      pred = pred.next;
    }


    return -1;
  }

  traversal() {
    let tempNode = this.head;

    for(let i = 0; i < this.size; i++) {
      console.log(tempNode.value, " =>");

      tempNode = tempNode.next;
    }
  }


}


const ll = new LinkedList();

ll.addAtIndex(0, 1);
ll.addAtIndex(1, 2);
ll.addAtIndex(2, 3);
ll.traversal();

console.log("--------------------------------------------------------");
ll.traversal();

ll.removeAtIndex(3);
console.log("--------------------------------------------------------");
ll.traversal();

console.log("--------------------------------------------------------");
console.log(ll.search(5));
