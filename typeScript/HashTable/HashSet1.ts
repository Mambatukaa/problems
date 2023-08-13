type LinkedListNode = {
  next: LinkedListNode | null;
  value: number;
}

export class MyHashSet {
  public bucket: Array<LinkedListNode | null>;
  public bucketsNumber: number;

  constructor(size: number) {
    this.bucketsNumber = size;

    this.bucket = new Array(size).fill(null);
  }

  _hash(value: number) {
    return value % this.bucketsNumber;
  }

  add(value: number): void {
    const bucketIndex = this._hash(value);
    const bucket = this.bucket[bucketIndex];

    const newNode = { value, next: null };

    if(!bucket) {
      this.bucket[bucketIndex] = newNode;

      return;
    }

    if(this.contains(value)) {
      console.log("The value exists in the set.")
      return;
    }

    let node: LinkedListNode | null = bucket

    while(node) {
      if(node.next == null) {
        node.next = newNode; 

        console.log("The value added!")

        return;
      }

      node = node.next;
    }

  }

  contains(value: number): boolean {
    const bucketIndex = this._hash(value);
    const bucket = this.bucket[bucketIndex];

    if(!bucket) {
      return false;
    }

    let node: LinkedListNode | null = bucket;

    while(node) {
      if(node.value === value) {
        return true;
      }

      node = node.next;
    }

    return false;
  }

  remove(value: number): void {
    const bucketIndex = this._hash(value);
    const bucket = this.bucket[bucketIndex];

    if(!bucket) {
      return;
    }

    // first element
    if(bucket.value === value) {
      this.bucket[bucketIndex] = bucket.next;
      return;
    }

    let prev: LinkedListNode | null = bucket;
    let node: LinkedListNode | null = bucket.next;

    while(node && prev) {
      if(node.value === value) {
        prev.next = node.next
        break;
      }
      
      prev = prev.next;
      node = node.next;
    }

    console.log("The value not found.")
  }

}


const set = new MyHashSet(5);

set.add(1);
set.add(6);
set.add(11);
set.add(12);

console.log(JSON.stringify(set.bucket));

set.remove(1);
set.remove(11);
set.remove(12);

console.log(JSON.stringify(set.bucket));


