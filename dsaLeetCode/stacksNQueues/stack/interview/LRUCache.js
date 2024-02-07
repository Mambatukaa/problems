
class ListNode {
  constructor(key, value) {
    this.value = value;
    this.key = key;
    this.prev = null;
    this.next = null;
  }
};

// Time Complexity: O(1)
// Space Complexity: O(k) k = capacity
class LRUCache {
  constructor(capacity) {
    this.capacity = capacity;
    this.cache = new Map();

    this.head = new ListNode(0, 0);
    this.tail = new ListNode(0, 0);

    this.head.next = this.tail;
    this.tail.prev = this.head;
  };

  put(key, value) {
    const node = new ListNode(key, value);

    if(this.cache.has(key)) {
      this.remove(this.cache.get(key));
    };

    // limit has reached. Remove old cache
    if(this.capacity === this.cache.size) {
      this.remove(this.tail.prev);
    };

    this.insert(node);
  };

  get(key) {
    if(!this.cache.has(key)) {
      return -1;
    };

    const node = this.cache.get(key);

    this.moveToHead(node);

    return node.value;
  };

  insert(node) {
    // set node to the cache
    this.cache.set(node.key, node);

    // insert to head
    const headNext = this.head.next;

    this.head.next = node;
    node.next = headNext;
    node.prev = this.head;
    headNext.prev = node;
  };

  remove(node) {
    this.cache.delete(node.key);

    node.prev.next = node.next;
    node.next.prev = node.prev;
  };

  moveToHead(node) {
    this.remove(node);
    this.insert(node);
  }
};

const lRUCache = new LRUCache(2);

lRUCache.put(2,1);
lRUCache.put(2,2);

console.log(lRUCache.get(2));





/*
 
 const cache = new LRUCache(2);

put(1, 1) ===> {1: 1}
put(2, 2) ===> {1: 1, 2: 2}

get(1) ==> 1 ===> {2: 2, 1: 1}

put(3, 3) ===> remove LRU (2) ===> {1:1} => put 3 ====> {3: 3, 1: 1}



Doubly LinkedList ====>  size = 2;

---> 1


head <=> 1 <=> tail;

---> 2

head <=> 2 <=> 1 <=> tail;

---> 3
-------> remove old element (1)

head <=> 3 <=> 2 <=> tail;

get(3) ====> update Least Recently Used cache

head <=> 2 <=> 3 <=> tail

 */
