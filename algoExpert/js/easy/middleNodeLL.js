// Time Complexity: O(n)
// Space Complexity: O(1)
const middleNode = (head) => {
  let curr = head;
  let length = 0;

  while(curr) {
    length++;
    curr = curr.next;
  }

  const half = Math.floor(length / 2);

  for(let i = 0; i < half; i++) {
    head = head.next;
  }

  console.log(head);

  return head;
}

// Fast and Slow
// Time Complexity: O(n)
// Space Complexity: O(1)
const middleNodeII = (head) => {
  let slow = head;
  let fast = head;

  while(fast && fast.next) {
    slow = slow.next;
    fast = fast.next.next;
  }

  console.log(slow);

  return slow;
}


class LinkedList {
  constructor(value) {
    this.value = value;
    this.next = null;
  }
}

const head = new LinkedList(2);

const node1 = new LinkedList(7);
const node2 = new LinkedList(3);
const node3 = new LinkedList(5);

const node4 = new LinkedList(4);

head.next = node1;
node1.next = node2;
node2.next = node3;
node3.next = node4;

middleNodeII(head);
