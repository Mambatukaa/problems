type LinkedList = {
  key: number,
  value: number,
  next: LinkedList | null;
}

class MyHashMap {
  public bucket: Array<LinkedList | null>;
  public bucketsNumber: number;

  constructor(size: number) {
    this.bucketsNumber = size;
    this.bucket = new Array(size).fill(null);
  }

  _hash(key: number): number {
    return key % this.bucketsNumber;
  }

  put(key: number, value: number): void {
    const bucketIndex = this._hash(key);
    const bucket = this.bucket[bucketIndex];

    const newNode: LinkedList = {
        key,
        value,
        next: null
      }

    if(!bucket) {
      this.bucket[bucketIndex] = newNode; 
      return;
    } 


    let node: LinkedList| null = bucket;

    while(node) {

      if(node.key === key) {
        node.value = value;
        return;
      } 


      if(node.next === null) {
        node.next = newNode;
      }

      node = node.next;
    }

  }


  get(key: number): number {
    const bucketIndex = this._hash(key);
    const bucket = this.bucket[bucketIndex];

    if(!bucket) {
      return -1;
    }

    let node: LinkedList | null = bucket;

    while(node) {
      if(node.key === key) {
        return node.value;
      }

      node = node.next;
    }

    return -1;

  }

  remove(key: number): void {
    const bucketIndex = this._hash(key);
    const bucket = this.bucket[bucketIndex];

    if(!bucket) {
      console.log("The bucket not exists!")
      return;
    }

    // first item
    if(bucket.key === key) {
      this.bucket[bucketIndex] = bucket.next;
    }


    let prev: LinkedList | null = bucket;
    let node: LinkedList | null = bucket.next;

    while(node && prev) {
      if(node.key === key) {
        prev.next = node.next;
      }

      prev = prev.next;
      node = node.next;
    }

    console.log("The value not found!");
  }



}

const map = new MyHashMap(5);

map.put(0,0);
map.put(1,1);
map.put(2,2);
map.put(5,6);

console.log(JSON.stringify(map.bucket));

map.remove(0);
map.remove(1);

console.log(JSON.stringify(map.bucket));
