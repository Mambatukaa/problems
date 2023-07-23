import { LinkedList } from '../lib/SinglyLinkedList';

class HashSet {
  public data: any[];
  public size: number;


  constructor(size: number) {
    this.data = new Array(size);
    this.size = size;
  }


  _hash(value: number): number {
    return value % this.size;
  }


  add(value: number): void {
    const index = this._hash(value);

    if(this.data[index]) {
      this.data[index].addAtIndex(3, value);

    } else {
      this.data[index] = new LinkedList();

      this.data[index].append(value);
    }

    console.log("Successfully added on the index of ", index);
  }


  remove(value: number): void {
    const index = this._hash(value);

    if(!this.data[index]) {
      console.log("Value not found!");

      return;
    }

    this.data[index].remove(value);
  }

}


const hashSet = new HashSet(5);
hashSet.add(1);
hashSet.add(2);

console.log(hashSet.data);


hashSet.remove(2);

console.log(hashSet.data);

